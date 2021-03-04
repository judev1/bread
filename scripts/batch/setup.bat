echo off

set system32=C:\Windows\System32
set system64=C:\Windows\SysWOW64

if exist "%system32%bread.bat" goto:eof
md "%system32%\bread"
copy "compiler.py" "%system32%\bread"
copy "interpreter.py" "%system32%\bread"
rename "bread32.bat" "bread.bat"
copy "bread.bat" "%system32%"
del "bread.bat"

if exist "%system64%bread.bat" goto:eof
md "%system64%\bread"
copy "compiler.py" "%system64%\bread"
copy "interpreter.py" "%system64%\bread"
rename "bread64.bat" "bread.bat"
copy "bread.bat" "%system64%"
del "bread.bat"

del "compiler.py"
del "interpreter.py"

