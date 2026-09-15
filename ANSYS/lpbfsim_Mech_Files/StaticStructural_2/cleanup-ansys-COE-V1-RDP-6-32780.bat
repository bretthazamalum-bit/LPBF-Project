@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="COE-V1-RDP-6" (taskkill /f /pid 22056)
if /i "%LOCALHOST%"=="COE-V1-RDP-6" (taskkill /f /pid 32120)
if /i "%LOCALHOST%"=="COE-V1-RDP-6" (taskkill /f /pid 23600)
if /i "%LOCALHOST%"=="COE-V1-RDP-6" (taskkill /f /pid 32780)

del /F cleanup-ansys-COE-V1-RDP-6-32780.bat
