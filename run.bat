@echo off
:: Pythonがインストールされているか確認
python --version >nul 2>&1

:: エラーレベルをチェックして、Pythonがインストールされていなかった場合は処理を中止
if %errorlevel% neq 0 (
    echo Pythonがインストールされていません。処理を中止します。
    pause
    exit /b 1
)

:: srcディレクトリ内のmain.pyを実行
python ./src/main.py

pause
