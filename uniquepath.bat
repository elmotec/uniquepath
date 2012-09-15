@echo off

for %%a in (%*) do (
    if "%%a" == "-h" goto nocall
    if "%%a" == "--help" goto nocall
    if "%%a" == "-d" goto nocall
    if "%%a" == "--debug" goto nocall
)

python.exe %~dp0\uniquepath.py %* > %TMP%\uniquepath_helper.bat
call %TMP%\uniquepath_helper.bat
goto end

:nocall
python.exe %~dp0\uniquepath.py %*

:end
exit /B %ERRORLEVEL%
