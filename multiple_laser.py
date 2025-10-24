#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mainWindow_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QHeaderView,QTableWidgetItem
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import re
import math
from typing import Optional


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.data: dict = {}
        self.ui.btnShowPlot.setDisabled(True)
        self.ui.btnSavePrg.setDisabled(True)
        pg.setConfigOptions(antialias=True)
        self.plot:PlotWidget = pg.PlotWidget()
        self.plot.setAspectLocked(ratio=1)  # 坐标轴等比例缩放
        self.plotCurrentFenquPoints = pg.ScatterPlotItem(
            size=self.ui.optHoleSize.value(), pen=None, brush=pg.mkBrush(255, 0, 255, 255), symbol='o')
        self.plotCurrentPoint = pg.ScatterPlotItem(
            size=self.ui.optHoleSize.value(), pen=None, brush='r', symbol='o')
        self.ui.graphLayout.addWidget(self.plot)
        self.ui.markerTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.initEvent()

    def initEvent(self):
        '''初始化UI界面事件绑定'''
        self.ui.btnShowPlot.clicked.connect(self.showPlot)
        self.ui.btnLoadPrg.clicked.connect(self.loadPrg)
        self.ui.btnSavePrg.clicked.connect(self.savePrg)

    def loadPrg(self):
        '''选择并导入镭射钻孔程序'''
        try:
            fileName, filetype = QFileDialog.getOpenFileName(self,
                                                            "选取镭射钻孔程序",
                                                            "./",
                                                            "所有文件 (*)")
            if fileName:
                self.data = {}
                self.plot.clear()
                self.ui.btnShowPlot.setDisabled(True)
                self.ui.btnSavePrg.setDisabled(True)
                self.data = loadPrg(fileName, self.ui.optThreshold.value())
                self.showPlot()
                self.ui.btnShowPlot.setEnabled(True)
                self.ui.btnSavePrg.setEnabled(True)
        except Exception as e:
                QMessageBox.critical(
                    self, '错误', '导入镭射加工程序时出现错误：\n'+e.args[0], QMessageBox.Ok)

    def savePrg(self):
        '''输出保存镭射分区加工程序'''
        if not self.data:
            QMessageBox.information(
                self, '提示', '请先导入镭射钻孔源程序。', QMessageBox.Ok)
        selected = QFileDialog.getSaveFileName(self, '输出分区加工程序')
        if selected:
            try:
                with open(selected[0], 'w', newline='\n') as f:
                    f.writelines(self.data['headers'])
                    for p in self.data['pre_markers']:
                        f.write(p.text)
                    f.write('T500\n')
                    for p in self.data['skiving_markers']:
                        f.write(p.text)
                    for fenqu in self.data['multiple_fenqu']:
                        for i,tool in enumerate(fenqu.tools):
                            f.write(tool+'\n')
                            if i==0:
                                for j,mark in enumerate(fenqu.markers):
                                    if j==len(fenqu.markers)-1:
                                        f.write('G83'+mark.text)
                                    else:
                                        f.write('G82'+mark.text)
                            for p in fenqu.tools_points[tool]:
                                f.write(p.text)
                    f.writelines(self.data['footers'])
                QMessageBox.information(
                    self, '完成', '已输出保存镭射分区加工程序。', QMessageBox.Ok)
            except Exception as e:
                QMessageBox.critical(
                    self, '错误', '输出分区镭射加工程序时出现错误：\n'+e.args[0], QMessageBox.Ok)

    def showPlot(self):
        '''根据导入的镭射钻孔程序数据绘制散点图'''
        self.plot.clear()
        if self.data:
            # 创建图表对象
            scatterSkiving = pg.ScatterPlotItem(size=self.ui.optMarkerSize.value(), pen=pg.mkPen(
                None), brush=pg.mkBrush(0, 255, 255, 255), symbol='s')
            scatterMarkers = pg.ScatterPlotItem(size=self.ui.optMarkerSize.value(), pen=pg.mkPen(
                None), brush=pg.mkBrush(255, 0, 255, 255),  symbol='+')
            scatterPoints = pg.ScatterPlotItem(size=self.ui.optHoleSize.value(), pen=pg.mkPen(
                None), brush=pg.mkBrush(255, 255, 255, 255), symbol='o')

            # 添加绘图数据
            scatterSkiving.addPoints(
                getPointsData(self.data['skiving_markers']))
            scatterMarkers.addPoints(getPointsData(self.data['pre_markers']))
            for fenqu in self.data['multiple_fenqu']:
                scatterMarkers.addPoints(getPointsData(fenqu.markers))
                for tool, points in fenqu.tools_points.items():
                    scatterPoints.addPoints(getPointsData(points))

            # 将图表对象加入UI图表中
            if self.ui.isShowFenquRect.isChecked():
                for fenqu in self.data['multiple_fenqu']:
                    self.plot.addItem(fenqu.getRegionRect())
            self.plot.addItem(scatterSkiving)
            self.plot.addItem(scatterMarkers)
            self.plot.addItem(scatterPoints)
            self.plot.addItem(self.plotCurrentFenquPoints)
            self.plot.addItem(self.plotCurrentPoint)

            # 绑定鼠标点击事件
            scatterSkiving.sigClicked.connect(self.pointClicked)
            scatterMarkers.sigClicked.connect(self.pointClicked)
            scatterPoints.sigClicked.connect(self.pointClicked)
            self.plotCurrentFenquPoints.sigClicked.connect(self.pointClicked)

    def pointClicked(self, plot, points):
        if len(points) > 0:

            point: Point = points[-1].data()
            self.ui.fenquNo.setText(str(point.fenqu))
            self.ui.toolNo.setText(point.tool)
            self.ui.posX.setText(str(point.x))
            self.ui.posY.setText(str(point.y))

            # 绘制鼠标选定的当前孔
            self.plotCurrentPoint.setSize(self.ui.optHoleSize.value())
            self.plotCurrentPoint.setData([{
                'pos': [point.x, point.y],
                'data': point
            }])

            # 绘制当前孔所在分区的全部孔
            if point.fenqu>0:
                for i,marker in enumerate(self.data['multiple_fenqu'][point.fenqu -1].markers):
                    if i<4:
                        self.ui.markerTable.setItem(i,0,QTableWidgetItem(str(marker.x)))
                        self.ui.markerTable.setItem(i,1,QTableWidgetItem(str(marker.y)))
                self.plotCurrentFenquPoints.clear()
                if self.ui.isShowFenquRect.isChecked() and point.fenqu > 0:
                    self.plotCurrentFenquPoints.setSize(self.ui.optHoleSize.value())
                    for tool, points in self.data['multiple_fenqu'][point.fenqu -
                                                                    1].tools_points.items():
                        self.plotCurrentFenquPoints.addPoints(
                            getPointsData(points))


class Point(object):
    '''用于保存坐标点数据，并提供两点间距离计算、坐标相等判定功能'''

    def __init__(self, x:float=0, y:float=0, fenqu:int=0, tool:str="", text:str=""):
        self.x:float = float(x)
        self.y:float = float(y)
        self.fenqu:int = fenqu
        self.tool:str = tool
        self.text:str = text

    def __sub__(self, v):
        return math.sqrt((self.x-v.x)**2+(self.y-v.y)**2)

    def __eq__(self, v):
        return (self.x == v.x and self.y == v.y)

    def __repr__(self):
        return "Point({x},{y})".format(**self.__dict__)

    def __str__(self):
        return "({x},{y})".format(**self.__dict__)


class MultipleLaser(object):
    '''用于保存镭射分区信息，包括对位点信息，对位点范围和每把刀加工坐标'''

    def __init__(self, markers: list[Point], index:int = 0):
        if type(markers) is not list or len(markers) != 4:
            raise ValueError('创建分区时必须提供4个对位点坐标！')
        self.index = index
        self.markers = markers
        self.center = None
        self.tools = []
        self.tools_points:dict = {}
        self.minX:Optional[float] = None
        self.minY:Optional[float] = None
        self.maxX:Optional[float] = None
        self.maxY:Optional[float] = None
        for p in self.markers:
            p.fenqu = index
            if self.minX is None or p.x < self.minX:
                self.minX = p.x
            if self.maxX is None or p.x > self.maxX:
                self.maxX = p.x
            if self.minY is None or p.y < self.minY:
                self.minY = p.y
            if self.maxY is None or p.y > self.maxY:
                self.maxY = p.y
        if self.minX is not None and self.minY is not None:
            self.center = Point((self.minX+self.maxX)/2,
                                (self.minY+self.maxY)/2,
                                fenqu=index)
        else:
            raise ValueError('创建分区时提供的对位点坐标不正确！')

    def addPoint(self, point: Point):
        '''将加工孔写入到对应的刀具列表中'''
        if point.tool not in self.tools:
            self.tools.append(point.tool)
            self.tools_points[point.tool] = []

        point.fenqu = self.index
        self.tools_points[point.tool].append(point)
        if point.x < self.minX:
            self.minX = point.x
        if point.x > self.maxX:
            self.maxX = point.x
        if point.y < self.minY:
            self.minY = point.y
        if point.y > self.maxY:
            self.maxY = point.y

    def isInRegion(self, x, y):
        '''判断坐标点是否在对位点包裹范围内'''
        minX=minY=maxX=maxY=None
        for marker in self.markers:
            if minX is None or marker.x < minX:
                minX = marker.x
            if maxX is None or marker.x > maxX:
                maxX = marker.x
            if minY is None or marker.y < minY:
                minY = marker.y
            if maxY is None or marker.y > maxY:
                maxY = marker.y
        return x >= minX and x <= maxX and y >= minY and y <= maxY
    

    def calcCenterDistance(self, x:float, y:float):
        '''计算坐标点和分区对位标靶中心点的距离值'''
        return math.sqrt((self.center.x-x)**2+(self.center.y-y)**2)

    def calcMarkerDistance(self,x:float,y:float):
        '''计算坐标点和最近的分区对位标靶点的距离值，当在分区内部时距离为负值'''
        if len(self.markers)==0:
            return None
        
        minX=minY=maxX=maxY=None
        for marker in self.markers:
            if minX is None or marker.x < minX:
                minX = marker.x
            if maxX is None or marker.x > maxX:
                maxX = marker.x
            if minY is None or marker.y < minY:
                minY = marker.y
            if maxY is None or marker.y > maxY:
                maxY = marker.y

        min_distance:Optional[float]=None
        if self.isInRegion(x,y):
            # 坐标在分区内部
            for marker in self.markers:
                distance = math.sqrt((marker.x-x)**2+(marker.y-y)**2)
                if min_distance is None or distance<min_distance:
                    min_distance=distance
            return -min_distance
        else:
            if minX<=x<=maxX:
                # 坐标在分区外部X轴范围内
                if y<=minY:
                    distance = minY - y
                else:
                    distance = y - maxY
                return distance
            elif minY<=y<=maxY:
                # 坐标在分区外部Y轴范围内
                if x<=minX:
                    distance = minX - x
                else:
                    distance = x - maxX
                return distance
            else:
                # 坐标在分区外部角上
                for marker in self.markers:
                    distance = math.sqrt((marker.x-x)**2+(marker.y-y)**2)
                    if min_distance is None or distance<min_distance:
                        min_distance=distance
                return min_distance

    def setIndex(self, index: int):
        '''重新设置分区索引编号'''
        self.index = index
        for p in self.markers:
            p.fenqu = index
        for tool, points in self.tools_points.items():
            for p in points:
                p.fenqu = index

    def getRegionRect(self):
        '''获取矩形'''
        plotRect = pg.PlotCurveItem(pen='r')
        if len(self.markers) == 0:
            return plotRect
        x = [self.minX, self.maxX, self.maxX, self.minX, self.minX]
        y = [self.minY, self.minY, self.maxY, self.maxY, self.minY]
        plotRect.setData(x, y)
        return plotRect


class getPointsData(object):
    '''将点对象数组转换为可迭代的 Pyqtgraph 绘图数据'''

    def __init__(self, points):
        self.points = points
        self.__index = None

    def __len__(self):
        return len(self.points)

    def __iter__(self):
        return self

    def __getitem__(self, index):
        point = self.points[index]
        return {
            'pos': [point.x, point.y],
            'data': point
        }

    def __next__(self):
        if self.__index is None:
            self.__index = 0
        if self.__index < len(self.points):
            point = self.points[self.__index]
            self.__index += 1
            return {
                'pos': [point.x, point.y],
                'data': point
            }
        else:
            self.__index = None
            raise StopIteration


def parsePos(s, leadingZero=True, length=3)->float:
    '''
    将文本坐标值转换为浮点数
    leadingZero: 是否为前导零格式，为False时表示为后导零格式（省略前导零）
    length: 前导零格式时表示整数的位数，后导零格式时表示小数的位数
    '''
    if type(s) is str:
        s = s.strip()
        if '.' in s:
            return float(s)
    elif type(s) in [float, int]:
        return float(s)
    else:
        raise ValueError('Invalid data type!')

    sign = 1
    if s[0:1] == "-":
        sign = -1
        s = s[1:]
    if leadingZero:
        # 前补零时 length 表示整数位数
        if len(s) < length:
            integer = s.ljust(length, '0')
            decimal = '0'
        else:
            integer = s[:length]
            decimal = s[length:]
    else:
        # 后补零时 length 表示小数位数
        if len(s) < length:
            integer = '0'
            decimal = s.rjust(length, '0')
        else:
            integer = s[:-length]
            decimal = s[-length:]
    return sign * float('{}.{}'.format(integer, decimal))


def getPoint(reg_match, fenqu=0, tool="", text=""):
    '''将正则匹配的坐标转换为点对象'''
    if reg_match and type(reg_match) is re.Match:
        groups = reg_match.groups()
        return Point(
            parsePos(groups[-2]),
            parsePos(groups[-1]),
            fenqu,
            tool,
            text
        )
    else:
        return None


def findFenquMarker(align_markers:list[Point], threshold:float=5.0):
    '''
    获取分区对位的四个对位点，左下角对位点为数组第一个点
    threshold 为对位点防呆距离的上限大小
    '''


    if len(align_markers) == 0:
        return None

    BL = align_markers[0]
    BR = None
    TL = None
    TR = None
    flag = False

    # 按照其它点与当前点的距离进行排序
    markers = sorted(align_markers,key=lambda v:(abs((v.x-BL.x)+abs(v.y-BL.y))))
    for i in range(1,len(markers)):
        # 获取分区右下角对位点
        point = markers[i]
        if point.x-BL.x > threshold and abs(point.y-BL.y) <= threshold:
            BR = point
            TL = None

            for i in range(1,len(markers)):
                # 获取分区左上角对位点
                point = markers[i]
                if point.y-BL.y > threshold and abs(point.x-BL.x) <= threshold and point != BR:
                    TL =point
                    TR = None
                    for i in range(1,len(markers)):
                        # 获取分区右上角对位点
                        point = markers[i]
                        if point.x-TL.x > threshold and point.y-BR.y > threshold and abs(point.x-BR.x) <= threshold and abs(point.y-TL.y) <= threshold and point != BR and point != TL:
                            TR = point
                            flag = True
                            break
                if flag:
                    break
        if flag:
            break
    if not flag:
        raise ValueError('没有找到左下方对位点{}对应的其它分区对位点！'.format(BL))

    # 从原列表中删除已获取的分区对位点
    result = [BL, BR, TR, TL]
    for i in range(len(align_markers)-1, -1, -1):
        if align_markers[i] in result:
            del align_markers[i]

    return result

def findFenquByMarker(point, fenqus:list[MultipleLaser]):
    '''根据点对象的坐标查找和分区对位点距离最近的分区'''
    min_distance = None         # 点坐标到分区对位点的最小距离
    in_region_flag = False      # 点坐标是否在分区对位点区域内
    index = None
    result = None

    if len(fenqus) == 0:
        return None

    for i, fenqu in enumerate(fenqus):
        distance = fenqu.calcMarkerDistance(point.x, point.y)
        if distance<0:
            # 点坐标在分区对位点区域内
            distance = -distance
            if min_distance == None or in_region_flag == False :
                in_region_flag = True
                min_distance = distance
                index = i
                result = fenqu
            elif distance < min_distance:
                min_distance = distance
                index = i
                result = fenqu
        elif in_region_flag==False and (min_distance == None or distance < min_distance):
            min_distance = distance
            index = i
            result = fenqu

    return (index+1, result)

def loadPrg(filepath:str, threshold:float=5)->dict:
    '''读取并分析激光钻孔分区程序'''
    headers = []
    footers = []
    pre_markers = []
    skiving_markers = []
    align_markers = []
    multiple_fenqu = []
    currentTool = ''

    with open(filepath, 'r') as f:
        # 读取程式头
        for line in f:
            line = line.strip()
            if line:
                headers.append(line+'\n')
            if line == '%':
                break

        # 读取预对位标靶
        pos_reg = re.compile(r'^(A|G82|G83)X(-?\d*)Y(-?\d*)$')
        for line in f:
            line = line.strip()
            if line == '':
                continue
            if line == 'T500':
                currentTool = 'T500'
                break
            pos_match = pos_reg.match(line)
            if not pos_match:
                raise ValueError('程序预对位指令不正确，请确认程序是否有误！')
            else:
                pre_markers.append(getPoint(pos_match, text=line+'\n'))

        # 读取烧标靶指令及分区对位点坐标
        tool_reg = re.compile(r'^T\d{1,2}$')
        pos_reg = re.compile(r'^(A|G82|G83)?X(-?\d*)Y(-?\d*)$')
        for line in f:
            line = line.strip()
            if line == '':
                continue
            if tool_reg.match(line):
                # 识别刀具指令
                currentTool = line
                break
            pos_match = pos_reg.match(line)
            if not pos_match:
                raise ValueError('烧靶坐标指令不正确，请确认程序是否有误！')

            pos = pos_match.groups()
            pos_str = 'X{}Y{}\n'.format(pos[1], pos[2])
            pos_x = parsePos(pos[1])
            pos_y = parsePos(pos[2])
            flag = True
            for mark in skiving_markers:
                if mark.text == pos_str:
                    flag = False
                    break
            if flag:
                skiving_markers.append(
                    Point(pos_x, pos_y, tool=currentTool, text=pos_str))
            if pos[0]:
                # 坐标前有对位指令，为对位点坐标点
                align_markers.append(
                    Point(pos_x, pos_y, tool=currentTool, text=pos_str))

        # 检查分区对位点
        if len(align_markers) == 0:
            raise ValueError('没有找到分区对位坐标点，请确认程序是否有误！')
        elif len(align_markers) % 4 != 0:
            raise ValueError('每个分区4个对位点，分区对位坐标点总数必须为4的倍数！')

        # 将分区对位点坐标按 x+y 从小到大排序
        align_markers.sort(key=lambda v: v.x+v.y)

        # 将对位点坐标按每个分区4个对位点进行分组
        while len(align_markers) > 0:
            index = len(multiple_fenqu)+1
            markers = findFenquMarker(align_markers, threshold)
            multiple_fenqu.append(MultipleLaser(markers, index))

        # 将分区顺序按照分区间的距离大小优化加工顺序
        for i in range(1,len(multiple_fenqu)-1):
            lastFenqu:MultipleLaser=multiple_fenqu[i-1]
            minDistance=multiple_fenqu[i].center-lastFenqu.center
            minIndex=i
            for j in range(i+1,len(multiple_fenqu)):
                if multiple_fenqu[j].center-lastFenqu.center<minDistance:
                    minDistance=multiple_fenqu[j].center-lastFenqu.center
                    minIndex=j
            if i!=minIndex:
                multiple_fenqu[i],multiple_fenqu[minIndex]=multiple_fenqu[minIndex],multiple_fenqu[i]
                multiple_fenqu[i].setIndex(i+1)
                multiple_fenqu[minIndex].setIndex(minIndex+1)


        # 读取加工点坐标，并保存到对应的分区中
        if currentTool is None or currentTool == 'T00' or currentTool == 'T0':
            raise ValueError('没有找到需要加工的孔坐标！')
        pos_reg = re.compile(r'^X(-?\d*)Y(-?\d*)$')
        m97_reg = re.compile(r'^(M97|M98),.*')
        m97_flag = ''
        for line in f:
            line = line.strip()

            # 跳过空行
            if line == '':
                continue

            if m97_reg.match(line):
                # 加工字唛指令
                m97_flag = line
                continue

            # 如果为烧字唛坐标
            if m97_flag:
                pos_match = pos_reg.match(line)
                point = getPoint(pos_match, tool=currentTool,
                                 text='{}\n{}\n'.format(m97_flag, line))
                if point:
                    index, fenqu = findFenquByMarker(point, multiple_fenqu)
                    point.fenqu = index
                    fenqu.addPoint(point)
                    m97_flag = ''
                    continue
                else:
                    raise ValueError('M97、M98字唛指令后必须为坐标！')

            # 如果为刀具指令
            if tool_reg.match(line):
                # 加工刀具指令
                currentTool = line
                if currentTool == 'T00' or currentTool == 'T0':
                    # 退刀指令，表示程序结束
                    footers.append('T00\n')
                    break
                continue

            # 如果为加工点坐标
            pos_match = pos_reg.match(line)
            if pos_match:
                point = getPoint(pos_match, tool=currentTool, text=line+'\n')
                index, fenqu = findFenquByMarker(point, multiple_fenqu)
                point.fenqu = index
                fenqu.addPoint(point)
                continue

            raise ValueError('无法识别的程序加工指令：\n'+line)

        for line in f:
            footers.append(line)

    return {
        'headers': headers,
        'pre_markers': pre_markers,
        'skiving_markers': skiving_markers,
        'multiple_fenqu': multiple_fenqu,
        'footers': footers
    }

if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec()
