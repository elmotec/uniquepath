@echo off

@rem remove any PYTHONHOME setting.
set PYTHONHOME=

if "%1" == "3" call uniquepath --remove *Python* --append C:\Python32 --append C:\Python32\scripts PATH
if "%1" == "2" call uniquepath --remove *Python* --append C:\Python27 --append C:\Python27\scripts PATH

exit /B %ERRORLEVEL%

