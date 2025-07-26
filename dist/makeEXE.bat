@echo off
REM "%~dp0" = here
cd /d "%~dp0"
cd ..
pyinstaller -w --onefile waveDoc.py