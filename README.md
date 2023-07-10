# MobaXtermKeygen-Python

# Usage
### Binary
```
xtgen.exe [name@req] [version@opt] [users@opt]
```
### Script
```
xtgen.py [name@req] [version@opt] [users@opt]
```

| Arg | Desc | State | Default |
|-|-| - | - |
| **user** | Username for license | required | |
| **version** | Version license to be generated for | optional | 23.2 |
| **users** | Number of users allowed for license | optional | 1 |

# Example:
```
xtgen.exe "Aetherx" 23.2 4
```

# Compile Binary
- Download [IronPython 3.x](https://github.com/IronLanguages/ironpython3/releases) and install to `x:\IronPython\3.4.0`
- Copy `xtgen.py` and place in same directory where `ipy.exe` exists
- Open `xtgen.py` and modify the header:
```
import sys
sys.path.append("Lib")

import os
import zipfile
```
- Open Windows Terminal / Command Prompt and execute `pip install pyinstaller`
- Execute `pyinstaller -Fw xtgen.py`
- New .exe will be placed in `x:\IronPython\3.4.0\dist\xtgen.exe`

# Notes
- Does not support IronPython 2.x; will return errors:
```
SyntaxError: unexpected token ':'
```
- If integrating with Visual Studio; best to use the binary solution. Attempting to run the .py will resort in a large list of .DLL library files required for operation. Turning into binary cuts all the .DLLs down into a single exe.
