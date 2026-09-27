@echo off
:: Navigate to the folder where this script lives
cd /d "%~dp0"

:: Run the python script
py workspace_manager.py

:: Keep the window open if an error occurs so you can read it
if %ERRORLEVEL% NEQ 0 pause