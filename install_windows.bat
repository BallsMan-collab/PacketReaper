@echo off
echo 🔥 Installing PacketReaper on Windows... 🔥

:: Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Python is not installed! Please install Python 3 from https://www.python.org/downloads/
    exit /b
)

:: Install required Python packages
pip install -r requirements.txt

echo ✅ Installation complete! Run PacketReaper with:
echo python packetreaper.py --mode sniff
pause
