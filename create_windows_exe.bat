@echo off
echo Flight Reservation App - Executable Creator
echo ========================================
echo.
echo This script will create a standalone Windows executable for the Flight Reservation App.
echo.

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH. Please install Python first.
    goto :EOF
)

echo Checking for required packages...
python -m pip show pyinstaller >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Installing PyInstaller...
    python -m pip install pyinstaller
)

echo Checking for required dependencies...
python -m pip install -r requirements.txt

echo.
echo Creating executable file...
echo.

pyinstaller --onefile --windowed --clean main.py

echo.
if %ERRORLEVEL% EQU 0 (
    echo Success! The executable has been created in the dist folder.
    echo You can find it at: %cd%\dist\main.exe
) else (
    echo There was an error creating the executable.
    echo Please check the output above for more information.
)

echo.
echo Press any key to exit...
pause >nul
