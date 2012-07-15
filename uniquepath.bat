@echo off

for %%a in (%*) do (
    if "%%a" == "-h" goto nocall
    if "%%a" == "--help" goto nocall
    if "%%a" == "-d" goto nocall
    if "%%a" == "--debug" goto nocall
)

C:\Python27\python.exe %~dp0\uniquepath.py %* > %TMP%\uniquepath_helper.bat
call %TMP%\uniquepath_helper.bat
goto end

:nocall
C:\Python27\python.exe %~dp0\uniquepath.py %*

:end
exit /B %ERRORLEVEL%
