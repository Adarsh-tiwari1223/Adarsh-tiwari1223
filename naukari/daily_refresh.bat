@echo off
title Naukri Daily Rank Booster - Adarsh Tiwari
cd /d "%~dp0\.."
echo ========================================================
echo    Naukri Daily Freshness Booster (Active Today)
echo    Adarsh Tiwari - QA Engineer / SDET
echo ========================================================
echo.
python naukari\naukri_updater.py refresh
echo.
echo ========================================================
echo Done! Your profile timestamp has been updated on Naukri.
echo ========================================================
timeout /t 5
