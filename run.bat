@echo off　
python --version >nul 2>&1

if %errorlevel% neq 0 (
    echo Pythonがインストールされていません。処理を中止します。
    pause
    exit /b 1
)


python ./src/main.py

pause
