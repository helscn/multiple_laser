# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 615)
        icon = QIcon()
        icon.addFile(u":/icon.ico", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, -1, 10)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(60)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.btnLoadPrg = QPushButton(self.centralwidget)
        self.btnLoadPrg.setObjectName(u"btnLoadPrg")
        self.btnLoadPrg.setMinimumSize(QSize(130, 30))
        self.btnLoadPrg.setMaximumSize(QSize(180, 16777215))
        font = QFont()
        font.setBold(True)
        self.btnLoadPrg.setFont(font)

        self.horizontalLayout_4.addWidget(self.btnLoadPrg)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(450, 16777215))
        font1 = QFont()
        font1.setBold(False)
        self.groupBox.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.optThreshold = QDoubleSpinBox(self.groupBox)
        self.optThreshold.setObjectName(u"optThreshold")
        self.optThreshold.setMinimumSize(QSize(80, 0))
        self.optThreshold.setMaximumSize(QSize(100, 16777215))
        self.optThreshold.setDecimals(1)
        self.optThreshold.setMinimum(0.100000000000000)
        self.optThreshold.setSingleStep(0.100000000000000)
        self.optThreshold.setValue(5.000000000000000)

        self.gridLayout_2.addWidget(self.optThreshold, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.optMarkerSize = QSpinBox(self.groupBox)
        self.optMarkerSize.setObjectName(u"optMarkerSize")
        self.optMarkerSize.setMinimumSize(QSize(80, 0))
        self.optMarkerSize.setMaximumSize(QSize(100, 16777215))
        self.optMarkerSize.setMinimum(-1)
        self.optMarkerSize.setMaximum(10)
        self.optMarkerSize.setSingleStep(1)
        self.optMarkerSize.setValue(8)

        self.gridLayout_2.addWidget(self.optMarkerSize, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.optHoleSize = QSpinBox(self.groupBox)
        self.optHoleSize.setObjectName(u"optHoleSize")
        self.optHoleSize.setMinimumSize(QSize(80, 0))
        self.optHoleSize.setMaximumSize(QSize(100, 16777215))
        self.optHoleSize.setMinimum(1)
        self.optHoleSize.setMaximum(1000)
        self.optHoleSize.setValue(4)

        self.gridLayout_2.addWidget(self.optHoleSize, 2, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.isShowFenquRect = QRadioButton(self.groupBox)
        self.isShowFenquRect.setObjectName(u"isShowFenquRect")
        self.isShowFenquRect.setChecked(True)

        self.horizontalLayout_5.addWidget(self.isShowFenquRect)

        self.isHideFenquRect = QRadioButton(self.groupBox)
        self.isHideFenquRect.setObjectName(u"isHideFenquRect")

        self.horizontalLayout_5.addWidget(self.isHideFenquRect)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnShowPlot = QPushButton(self.groupBox)
        self.btnShowPlot.setObjectName(u"btnShowPlot")
        self.btnShowPlot.setMinimumSize(QSize(80, 45))
        self.btnShowPlot.setMaximumSize(QSize(100, 16777215))
        self.btnShowPlot.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnShowPlot)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(450, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.fenquNo = QLineEdit(self.groupBox_2)
        self.fenquNo.setObjectName(u"fenquNo")
        self.fenquNo.setMinimumSize(QSize(60, 0))
        self.fenquNo.setMaximumSize(QSize(80, 16777215))
        self.fenquNo.setReadOnly(True)

        self.gridLayout_3.addWidget(self.fenquNo, 0, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(80, 16777215))
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_20, 0, 2, 1, 1)

        self.posX = QLineEdit(self.groupBox_2)
        self.posX.setObjectName(u"posX")
        self.posX.setMinimumSize(QSize(60, 0))
        self.posX.setMaximumSize(QSize(80, 16777215))
        self.posX.setReadOnly(True)

        self.gridLayout_3.addWidget(self.posX, 1, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(80, 16777215))
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(80, 16777215))
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(80, 16777215))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_7, 1, 2, 1, 1)

        self.posY = QLineEdit(self.groupBox_2)
        self.posY.setObjectName(u"posY")
        self.posY.setMinimumSize(QSize(60, 0))
        self.posY.setMaximumSize(QSize(80, 16777215))
        self.posY.setReadOnly(True)

        self.gridLayout_3.addWidget(self.posY, 1, 3, 1, 1)

        self.toolNo = QLineEdit(self.groupBox_2)
        self.toolNo.setObjectName(u"toolNo")
        self.toolNo.setMinimumSize(QSize(60, 0))
        self.toolNo.setMaximumSize(QSize(80, 16777215))
        self.toolNo.setReadOnly(True)

        self.gridLayout_3.addWidget(self.toolNo, 0, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.markerTable = QTableWidget(self.groupBox_2)
        if (self.markerTable.columnCount() < 2):
            self.markerTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.markerTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.markerTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.markerTable.rowCount() < 4):
            self.markerTable.setRowCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setText(u"1");
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.markerTable.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.markerTable.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.markerTable.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.markerTable.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.markerTable.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.markerTable.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.markerTable.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.markerTable.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.markerTable.setItem(2, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.markerTable.setItem(2, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.markerTable.setItem(3, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.markerTable.setItem(3, 1, __qtablewidgetitem13)
        self.markerTable.setObjectName(u"markerTable")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.markerTable.sizePolicy().hasHeightForWidth())
        self.markerTable.setSizePolicy(sizePolicy)
        self.markerTable.setMinimumSize(QSize(280, 150))
        self.markerTable.setMaximumSize(QSize(320, 150))
        self.markerTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.markerTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.markerTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.markerTable)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.graphLayout = QVBoxLayout()
        self.graphLayout.setObjectName(u"graphLayout")
        self.graphLayout.setContentsMargins(20, 10, 10, 10)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btnSavePrg = QPushButton(self.centralwidget)
        self.btnSavePrg.setObjectName(u"btnSavePrg")
        self.btnSavePrg.setMinimumSize(QSize(130, 30))
        self.btnSavePrg.setMaximumSize(QSize(180, 16777215))
        self.btnSavePrg.setFont(font)

        self.horizontalLayout_3.addWidget(self.btnSavePrg)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.graphLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.graphLayout)

        self.horizontalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u956d\u5c04\u81ea\u52a8\u5206\u533a\u8f6c\u6362\u7a0b\u5e8f V20251025", None))
        self.btnLoadPrg.setText(QCoreApplication.translate("MainWindow", u"\u8f7d\u5165\u6e90\u7a0b\u5e8f...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u4f4d\u70b9\u9632\u53cd\u9608\u503c\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u4f4d\u70b9\u663e\u793a\u5927\u5c0f\uff1a", None))
        self.optMarkerSize.setSuffix("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5de5\u5b54\u663e\u793a\u5927\u5c0f\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5206\u533a\u8fb9\u754c\u7ebf\uff1a", None))
        self.isShowFenquRect.setText(QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.isHideFenquRect.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.btnShowPlot.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u5206\u533a\n"
"\u793a\u610f\u56fe", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u9009\u5b9a\u5b54\u4fe1\u606f", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u5200\u5177\u7f16\u53f7", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u5206\u533a\u7f16\u53f7", None))
        self.label_12.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5206\u533a\u5bf9\u4f4d\u70b9\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        ___qtablewidgetitem = self.markerTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X\u5750\u6807", None));
        ___qtablewidgetitem1 = self.markerTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Y\u5750\u6807", None));
        ___qtablewidgetitem2 = self.markerTable.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.markerTable.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.markerTable.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"4", None));

        __sortingEnabled = self.markerTable.isSortingEnabled()
        self.markerTable.setSortingEnabled(False)
        self.markerTable.setSortingEnabled(__sortingEnabled)

        self.btnSavePrg.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u5206\u533a\u7a0b\u5e8f...", None))
    # retranslateUi

