@echo off
title Naukri Automated Profile Updater - Adarsh Tiwari
cd /d "%~dp0\.."
echo ========================================================
echo    Naukri Profile Automatic Updater
echo    Adarsh Tiwari - QA Engineer / SDET
echo ========================================================
echo.
python naukari\naukri_updater.py update
echo.
echo ========================================================
echo Process finished. Press any key to close this window.
echo ========================================================
pause
