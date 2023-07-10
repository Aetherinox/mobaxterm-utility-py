# MobaXtermKeygen-Python

## Usage
### Binary
```bash
mobaxtgen_cli.exe [OPTIONS] <name> <version> <users>
```
### Script
```bash
mobaxtgen_cli.py [OPTIONS] <name> <version> <users>
```

#### Options
| Arg | Desc |
|-|-|
| `-s` | Output simple result |
| `-h` | Help information |

#### Arguments

|  | Desc | State | Default |
|-|-| - | - |
| **user** | Username for license | required | |
| **version** | Version license to be generated for | optional | 23.2 |
| **users** | Number of users allowed for license | optional | 1 |

## Example:
Generate + return normal result
```bash
$ mobaxtgen_cli.exe "Aetherx" 23.2 4
```
Output:
```ini
Created File .............: X:\XmobaTerms\Custom.mxtpro
Username .................: Aetherx
License Enc ..............: 2sWCtwDItoDM0o3e6tGfrp3e7pnf6tGerh3a4tG
License Str ..............: 1#Aetherx|232#4#233262#0#0#0#
Version ..................: 23.2
Users ....................: 4
```

---

Generate + return simple result
```bash
$ mobaxtgen_cli.exe -s "Aetherx" 23.2 4
```

Output:
```ini
2sWCtwDItoDM0o3e6tGfrp3e7pnf6tGerh3a4tG
```

## Compile Binary
- Download [IronPython 3.x](https://github.com/IronLanguages/ironpython3/releases) and install to `x:\IronPython\3.4.0`
- Copy `xtgen.py` and place in same directory where `ipy.exe` exists
- Open `xtgen.py` and modify the header:

```py
import sys
sys.path.append("Lib")

import os
import zipfile
```

- Open Windows Terminal / Command Prompt and execute `pip install pyinstaller`
- Execute the following command in terminal:

```bash
pyinstaller -Fwc xtgen.py --version-file=verinfo.py
```

  > If you do not add `c` to the list of arguments, the exe will output nothing to console.
- New .exe will be placed in `x:\IronPython\3.4.0\dist\xtgen.exe`

# Todo
May add argument parser later. The script is pretty simple, no need to complicate it.

## Notes
- Does not support IronPython 2.x; will return errors:
```
SyntaxError: unexpected token ':'
```
- If integrating with Visual Studio; best to use the binary solution. Attempting to run the .py will resort in a large list of .DLL library files required for operation. Turning into binary cuts all the .DLLs down into a single exe.
