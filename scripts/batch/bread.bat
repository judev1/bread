@echo off

>nul python --version 3
if errorlevel 1 goto notinstalled

set operation=%1
set system32=C:\Windows\SysWOW64

if not defined operation goto lost
if %operation%==run goto file
if %operation%==compile goto file
if %operation%==help goto help
goto lost

:file
set file=%2
if not defined file goto nofile
if not exist %file% goto notexists
echo %file%>"file.txt"
if %operation%==run goto run
if %operation%==compile goto compile

:run
python %system32%\bread\interpreter.py
goto:eof

:compile
python %system32%\bread\compiler.py
goto:eof

:help
echo  Usage: bread [run^|compile] path\to\file
echo.
echo         run - Runs the .brr file specified
echo     compile - Compiles a .brr into a .py file or vice versa
echo    filepath - The file to perform the operation on
goto:eof

:notinstalled
echo Python must be installed to use bread
goto:eof

:lost
echo Command not recognised, use 'bread help' for more info
goto:eof

:nofile
echo No file specified
goto:eof

:notexists
echo '%file%' does not exist
goto:eof