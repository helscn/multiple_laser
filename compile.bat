@echo off
SETLOCAL ENABLEEXTENSIONS

IF "%1"=="" (
	ECHO.
	SET /P compile_file=��������Ҫ����� Python �ű��ļ�·����
) ELSE (
	SET compile_file=%1
)
IF NOT EXIST "%compile_file%" (
	ECHO.
	ECHO ָ���Ľű��ļ������ڣ�
	GOTO END
)

FOR /F "delims=" %%A IN ('"echo %compile_file%"') do (
	SET compile_path=%%~dpA
	SET compile_name=%%~nA
)

ECHO.
SET /P app_name=����������ĳ����ļ�����Ĭ��Ϊ %compile_name% ��
IF DEFINED app_name (
	SET compile_name=--name %app_name%
) ELSE (
	SET compile_name=--name %compile_name%
)

IF EXIST icon.ico (
	SET package_icon=--icon "%compile_path%\icon.ico"
) ELSE (
	SET package_icon= 
)

ECHO.
choice /C FD /M ��ѡ����ģʽ�����Ϊ���ļ�[F]�����Ǵ��Ϊ���ļ���[D]��
IF ERRORLEVEL 2 SET compile_mode=--onedir
IF ERRORLEVEL 1 SET compile_mode=--onefile

ECHO.
choice /C YN /M ����ʱ�Ƿ���ʾ����̨���ڣ�
IF ERRORLEVEL 2 SET show_console=--console
IF ERRORLEVEL 1 SET show_console=--noconsole

ECHO.
IF EXIST "%compile_path%\.env\Scripts\activate.bat" (
	ECHO ���ڼ���ű����е� Python ���⻷��...
	CALL "%compile_path%\.env\Scripts\activate.bat"
)
IF EXIST %compile_path%\.venv\Scripts\activate.bat (
	ECHO ���ڼ���ű����е� Python ���⻷��...
	CALL "%compile_path%\.venv\Scripts\activate.bat"
)

ECHO.
ECHO PyInstaller %compile_mode% %show_console% %package_icon% %compile_name% %compile_file%
pyinstaller %compile_mode% %show_console% %package_icon% %compile_name% %compile_file%
IF ERRORLEVEL 1 (
	ECHO.
	ECHO ��� Python �ű�ʱ���ִ���! 
) ELSE (
	ECHO.
	ECHO  �ű� %compile_file% �����ɡ�
)

IF EXIST "%compile_path%\.env\Scripts\deactivate.bat" (
	ECHO.
	ECHO �����˳��ű����е� Python ���⻷��...
	CALL "%compile_path%\.env\Scripts\deactivate.bat"
)
IF EXIST "%compile_path%\.venv\Scripts\deactivate.bat" (
	ECHO.
	ECHO �����˳��ű����е� Python ���⻷��...
	CALL "%compile_path%\.venv\Scripts\deactivate.bat"
)
ECHO.
PAUSE