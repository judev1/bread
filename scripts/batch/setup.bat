echo off

set system32=C:\Windows\SysWOW64

md "%system32%\bread"
move "compiler.py" "%system32%\bread"
move "interpreter.py" "%system32%\bread"
move "bread.bat" "%system32%"