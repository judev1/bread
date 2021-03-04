  !include "MUI2.nsh"
  !include x64.nsh

  Name "Bread"
  OutFile "breadinstaller.exe"
  Unicode True
  
  InstallDir "$PROFILE\AppData\local\programs\bread"
  RequestExecutionLevel admin

  !define SYSTEM32 "C:\Windows\System32"
  !define SYSTEM64 "C:\Windows\SysWOW64"

  !define MUI_ICON "images\bread.ico"
  !define MUI_WELCOMEFINISHPAGE_BITMAP "images\breadlong.bmp"

  !define MUI_UNICON "images\bread.ico"
  !define MUI_UNWELCOMEFINISHPAGE_BITMAP "images\breadlong.bmp"

  !insertmacro MUI_PAGE_WELCOME
  !insertmacro MUI_PAGE_LICENSE "License.md"
  !insertmacro MUI_PAGE_DIRECTORY
  !insertmacro MUI_PAGE_INSTFILES
  !insertmacro MUI_PAGE_FINISH

  !insertmacro MUI_UNPAGE_WELCOME
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES
  !insertmacro MUI_UNPAGE_FINISH

  !insertmacro MUI_LANGUAGE "English"

Section "Install"
  SetOutPath "$INSTDIR"
  File "README.md"
  File "scripts\python\compiler.py"
  File "scripts\python\interpreter.py"
  File "scripts\batch\bread32.bat"
  File "scripts\batch\bread64.bat"
  File "scripts\batch\setup.bat"
  ExecWait "$INSTDIR\setup.bat"
  Delete "$INSTDIR\setup.bat"
  WriteUninstaller "uninstall.exe"
SectionEnd

Section "Uninstall"
  Delete "$INSTDIR\README.md"
  Delete "${SYSTEM32}\bread.bat"
  Delete "${SYSTEM64}\bread.bat"
  Delete "${SYSTEM32}\bread\interpreter.py"
  Delete "${SYSTEM32}\bread\compiler.py"
  Delete "${SYSTEM64}\bread\interpreter.py"
  Delete "${SYSTEM64}\bread\compiler.py"
  Delete "$INSTDIR\uninstall.exe"
  RMDir "${SYSTEM32}\bread"
  RMDir "${SYSTEM64}\bread"
  RMDir "$INSTDIR"
SectionEnd
