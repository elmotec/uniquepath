@rem remove any PYTHONHOME setting.
@set PYTHONHOME=

@rem first sets python path so we can run uniquepath.
@set PYTHON=C:\Python%1
@dir %PYTHON% > NUL
@if ERRORLEVEL 1 GOTO FAILED

@set PATH=%PATH%;%PYTHON%
call uniquepath --remove *Python* --append %PYTHON% --append %PYTHON%\Scripts PATH
@goto SUCCESS

:FAILED
@echo %PYTHON% is not a valid directory.
@set ERRORLEVEL=1

:SUCCESS
@exit /B %ERRORLEVEL%

