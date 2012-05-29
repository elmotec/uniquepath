@echo off

for %%a in (%*) do (
    if "%%a" == "-h" goto help
)

C:\Python27\python.exe %~dp0\uniquepath.py %* > %TMP%\uniquepath_helper.bat
call %TMP%\uniquepath_helper.bat
goto end

:help
uniquepath.py -h 

:end
exit /B %ERRORLEVEL%
