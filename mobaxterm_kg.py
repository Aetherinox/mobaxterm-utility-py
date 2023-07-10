#/usr/bin/env python3

#
#   includes
#

import sys
sys.path.append("Lib")

import os
import zipfile
# import argparse

#
#   vars
#

__script__                  = "MobaXterm Generator"
__output__                  = "Custom.mxtpro"
__py__                      = os.path.basename(__file__)
__path__                    = os.path.join(os.getcwd( ), __output__)
__desc__                    = """A license generator for MobaXterm."""
__version_info__            = ( '1', '0', '0', '0' )
__version__                 = '.'.join(__version_info__)
__bFlag__                   = False

#
#   arg parsing
#
#   may add this later. right now the script is simple and works great.
#   if you want to add it, have at it.
#

#   parser  = argparse.ArgumentParser( prog=__py__, description=__desc__, epilog=__version__)
#   group   = parser.add_mutually_exclusive_group()
#
#   group.add_argument("-s", "--simple", help="show simple output", action="store_true")
#   group.add_argument("-u", "--usage", help="helpful usage examples", action="store_true")

#   parser.add_argument("name", type=str, help="name of user", required=True)
#   parser.add_argument("version", type=int, help="version of mobaxterm running")
#   parser.add_argument("users", type=int, help="Number of users license is good for")

#   args = parser.parse_args()

#
#   Help
#

def About( ):
    print( )
    print( )
    print( '-------------------------------------------------------------' )
    print( '%s v%s' % (__script__, __version__) )
    print( __desc__ )
    print( '-------------------------------------------------------------' )
    print( )
    print( 'Usage:')
    print( )
    print( '    %s [OPTIONS] [ARGS]' % __py__ )
    print( )
    print( 'Options:')
    print( )
    print( '    -h ............. show this help message' )
    print( '    -s ............. output simple license key instead of full details' )
    print( )
    print( 'Arguments:')
    print( )
    print( '    name ........... Name of user license belongs to.' )
    print( )
    print( '    version ........ Version of MobaXterm running.' )
    print( '                     Example:    23.2' )
    print( '                     Default:    23.2' )
    print( )
    print( '    count .......... Number of user licenses.' )
    print( '                     Default:    1' )
    print( '                     Example:    2' )
    print( )
    print( 'Example:')
    print(  )
    print( '    You can use any of the following examples below to format your command:' )
    print(  )
    print( '    %s Aetherx 23.2 2            ..... v23.2 - 2 users' % __py__ )
    print( '    %s Aetherx 23.2              ..... v23.2 - 1 user' % __py__ )
    print( '    %s "Aetherx" 23.2 2          ..... v23.2 - 2 users' % __py__ )
    print( '    %s "Aetherx" "23.2" "5"      ..... v23.2 - 5 users' % __py__ )
    print( '    %s -s "Aetherx" "23.2" "1"   ..... v23.2 - 1 user - simple output' % __py__ )
    print( )
    print( )
    sys.exit( 0 )

#
#   arg > options
#
#   better ways of doing dynamic arguments counts but since we'll never
#   need that. quick solution.
#
#   possibly later to add ( argument parse )
#   If you want to add this yourself, go for it
#       import argparse
#       parser = argparse.ArgumentParser()
#

if sys.argv[ 1 ].startswith('-'):
    __bFlag__ = True

#
#   argument > command information
#

if __bFlag__ and sys.argv[ 1 ].startswith('-h'):
    About()

#
#   arg1 / name
#       Example:    Aetherx
#

try:
    name
except NameError:
    pos = 1
    if __bFlag__:
        pos = 2

    if len( sys.argv ) > pos:
        name = sys.argv[ pos ]
    else:
        print( 'Missing arguments -- provide a name' )
        sys.exit( 0 )

#
#   arg2 / version
#       Example:    23.2
#

try:
    ver
except NameError:
    pos = 2
    if __bFlag__:
        pos = 3

    if len( sys.argv ) > pos:
        ver = sys.argv[ pos ]
    else:
        ver = "23.2"

#
#   arg3 / users
#       Example:    5
#       Default:    1
#

try:
    users
except NameError:
    pos = 3
    if __bFlag__:
        pos = 4

    if len( sys.argv ) > pos:
        users = int( sys.argv[ pos ] )
    else:
        users = int(1)

#
#   License Types
#       Don't change ENUMs, these are programmed in mobaxterm
#

class LicenseType:
    Professional    = 1
    Educational     = 3
    Persional       = 4

#
#   base64 alphabet
#

_b64Str  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

#
#   dictionary
#   {
#       0: 'A',     1: 'B',     2: 'C',     3: 'D',
#       4: 'E',     5: 'F',     6: 'G',     7: 'H',
#       8: 'I',     9: 'J',     10: 'K',    11: 'L',
#       12: 'M',    13: 'N',    14: 'O',    15: 'P',
#       16: 'Q',    17: 'R',    18: 'S',    19: 'T',
#       20: 'U',    21: 'V',    22: 'W',    23: 'X',
#       24: 'Y',    25: 'Z',    26: 'a',    27: 'b',
#       28: 'c',    29: 'd',    30: 'e',    31: 'f',
#       32: 'g',    33: 'h',    34: 'i',    35: 'j',
#       36: 'k',    37: 'l',    38: 'm',    39: 'n',
#       40: 'o',    41: 'p',    42: 'q',    43: 'r',
#       44: 's',    45: 't',    46: 'u',    47: 'v',
#       48: 'w',    49: 'x',    50: 'y',    51: 'z',
#       52: '0',    53: '1',    54: '2',    55: '3',
#       56: '4',    57: '5',    58: '6',    59: '7',
#       60: '8',    61: '9',    62: '+',    63: '/',
#       64: '='
#   }
#

_dict = { i : _b64Str [i] for i, v in enumerate(_b64Str) }

#
#   base64 > encode
#       byteString  :   b'6k\t-< -:04z{zkykz{{z~zkxkxkxk'       (Aetherx)
#

def Encode(byteString : bytes):
    print( byteString )
    res = b''

    # divmod( dividend / divisor )
    i_blk, left_bytes = divmod( len(byteString), 3 )

    for i in range(i_blk):
        coding_int = int.from_bytes( byteString[ 3 * i:3 * i + 3 ], 'little' )
        blk = _dict[ coding_int & 0x3f ]
        blk += _dict[ ( coding_int >> 6 ) & 0x3f ]
        blk += _dict[ ( coding_int >> 12 ) & 0x3f ]
        blk += _dict[ ( coding_int >> 18 ) & 0x3f ]
        res += blk.encode( )

    if left_bytes == 0:
        return res
    elif left_bytes == 1:
        coding_int = int.from_bytes( byteString[ 3 * i_blk: ], 'little' )
        blk = _dict[ coding_int & 0x3f ]
        blk += _dict[ ( coding_int >> 6 ) & 0x3f ]
        res += blk.encode( )

        return res
    else:
        coding_int = int.from_bytes( byteString[ 3 * i_blk: ], 'little' )
        blk = _dict[ coding_int & 0x3f ]
        blk += _dict[ ( coding_int >> 6 ) & 0x3f ]
        blk += _dict[ ( coding_int >> 12 ) & 0x3f ]
        res += blk.encode( )

        return res

#
#   base64 > encrypt
#       key         :   1927
#       byteString  :   b'1#Aetherx|232#1#233262#0#0#0#'
#

def Encrypt( key : int, byteString : bytes ):
    # bytearray(b'')
    res = bytearray( )

    for i, v in enumerate( byteString ):
        res.append(byteString[i] ^ ((key >> 8) & 0xff))
        key = res[ -1 ] & key | 0x482D

    # b'6'
    # b'6k'
    # ....
    # b'6k\t-< -:04z{zkykz{{z~zkxkxkxk'
    return bytes( res )

#
#   Generate License
#

def GenLicense(license : LicenseType, users : int, username : str, ver_major : int, ver_minor):
    assert( users >= 0 )

    #   License String
    #
    #   1#aetherx|232#99#233262#0#0#0#
    #   {0}#{1}|{2}{3}#{4}#{2}3{3}6{3}#{5}#{6}#{7}#
    #       0 : license type
    #       1 : username
    #       2 : ver_major
    #       3 : ver_minor
    #       4 : users
    #       5 : 0
    #       6 : 0
    #       7 : 0
    #
    #   Structure:  license_type # username | ver_major ver_minor # users # ver_major 3 ver_minor 6 ver_minor # 0 # 0 # 0 #

    lic_str         = '%d#%s|%d%d#%d#%d3%d6%d#%d#%d#%d#' % (license, username, ver_major, ver_minor, users, ver_major, ver_minor, ver_minor, 0, 0, 0)
    lic_enc         = Encode(Encrypt(0x787, lic_str.encode( ))).decode( )

    with zipfile.ZipFile( __output__, 'w' ) as zipFile:
        zipFile.writestr( 'Pro.key', data = lic_enc )

    return ( lic_enc, lic_str )

if not name or not ver:
    print('Fatal Error: Not enough arguments')
else:

    #   version structure
    ver_major, ver_minor    = ver.split( '.' )[ 0:2 ]
    ver_major               = int( ver_major )
    ver_minor               = int( ver_minor )
    users                   = int( users )

    #   Generate license key

    results                 = GenLicense( LicenseType.Professional, users, name, ver_major, ver_minor )
    v_license_enc           = results[ 0 ]
    v_license_str           = results[ 1 ]
    v_license_path          = __output__
    v_license_name          = name
    v_license_users         = users
    v_license_ver           = ver

#
#   Output > Full
#
#   Show all information related to license generation.
#

def OutputFull():
    #   Output to console
    print( )
    print()
    print( 'Created File .............: %s' % __path__ )
    print( 'Username .................: %s' % v_license_name )
    print( 'License Enc ..............: %s' % v_license_enc )
    print( 'License Str ..............: %s' % v_license_str )
    print( 'Version ..................: %s' % v_license_ver )
    print( 'Users ....................: %s' % v_license_users )
    print( )
    print( )

#
#   Output > Simple
#
#   Only show encrypted license key used in license file.
#

def OutputSimple():
    print( v_license_enc )

#
#   Determine output
#

if __bFlag__ and sys.argv[ 1 ].startswith('-s'):
    OutputSimple()
else:
    OutputFull()