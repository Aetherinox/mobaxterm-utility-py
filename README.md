# MobaXtermKeygen-Python

# Compile
- Download IronPython 3.x and install to `x:\IronPython\3.4.0`
- Copy `xtgen.py` and place in same directory where ipy.exe exists
- Open xtgen.py and modify the header:
```
import sys
sys.path.append("Lib")

import os
import zipfile
```
- Open Windows Terminal / Command Prompt and execute `pip install pyinstaller`
- Execute `pyinstaller -Fw xtgen.py`
- New .exe will be replaced in `x:\IronPython\3.4.0\dist\xtgen.exe`
