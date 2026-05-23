@echo off
title Government Accident Detection System
cd /d "%~dp0backend"
echo Starting Government Accident Detection System...
echo.
echo Keep this window open while using the website.
echo Website will open at http://127.0.0.1:8000
echo.
start "" "http://127.0.0.1:8000"
python run.py
pause
