# # #
#   @name       : pyinstaller version template
#   @desc       : for use with pyinstaller
#                 pyinstaller -Fwc yourscript.py --version-file=versioninfo.py
#   @author     : Aetherinox
#   @update     : 07.18.24
#   @url        : https://github.com/Aetherinox/mobaxterm-utility-py
#
#   make sure this is saved as UTF-8
# # #

VSVersionInfo(
  ffi=FixedFileInfo(
    #   always a tuple with four items: (1, 2, 3, 4)
    #   Set not needed items to zero 0.
    filevers=(1, 2, 0, 0),
    prodvers=(1, 2, 0, 0),

    #   bitmask which specifies the valid bits 'flags'r
    mask=0x17,

    #   Cbitmask which specifies the Boolean attributes of the file.
    flags=0x0,

    #   The OS which this file was designed.
    #   0x4 = NT
    OS=0x4,

    #   Type of file.
    #   0x1 = application (exe)
    fileType=0x1,

    #   Function for file.
    #   0x0 = function not defined
    subtype=0x0,

    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904b0',
        [StringStruct(u'CompanyName', u'Aetherx'),
        StringStruct(u'FileDescription', u'Command-line license utility for MobaXterm'),
        StringStruct(u'FileVersion', u'1, 2, 0, 0'),
        StringStruct(u'InternalName', u'mobaxtgen_cli'),
        StringStruct(u'LegalCopyright', u'(c)2024 Aetherinox - All rights reserved.'),
        StringStruct(u'OriginalFilename', u'mobaxtgen_cli.exe'),
        StringStruct(u'ProductName', u'MobaXterm CLI License Utility'),
        StringStruct(u'ProductVersion', u'1.2.0.0'),
        StringStruct(u'CompanyShortName', u'Aetherx'),
        StringStruct(u'ProductShortName', u'Mobaxt CLI'),
        StringStruct(u'LastChange', u'3a13412b14aa626613a72fcfb27652eaa3a4a725-refs/branch-heads/1001@{#145}'),
        StringStruct(u'Official Build', u'1')])
      ]),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
