# Embedded file name: sdcard/com.hipipal.qpyplus/scripts/inunxl@bs/ServerConfig.py
import os
import ServerInfo
import sys
import zlib
import base64
import binascii
import time
W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[1;32m'
O = '\x1b[33m'
B = '\x1b[34m'
P = '\x1b[35m'
C = '\x1b[36m'
GR = '\x1b[37m'

def color(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.0 / 90)


yess = 'simpleconfig.ini'
no = 'simpleserver.ini'
try:
    Lock = open(os.path.join(sys.path[0], yess), 'rb').read()
    open(os.path.join(sys.path[0], no), 'wb').write(zlib.compress(binascii.b2a_qp(binascii.b2a_base64(zlib.compress(binascii.b2a_base64(zlib.compress(base64.b32encode(zlib.compress(zlib.compress(zlib.compress(binascii.b2a_hex(base64.b32encode(zlib.compress(zlib.compress(base64.b16encode(zlib.compress(Lock)))))))))))))))))
except:
    pass

try:
    read_lock = open(os.path.join(sys.path[0], no), 'rb').read()
except:
    sys.exit()

class Sets:

    def __init__(self):
        self.Config = ''
        self.load()

    def load(self):
        for name, value in [ line.split(' = ') for line in zlib.decompress(base64.b16decode(zlib.decompress(zlib.decompress(base64.b32decode(binascii.a2b_hex(zlib.decompress(zlib.decompress(zlib.decompress(base64.b32decode(zlib.decompress(binascii.a2b_base64(zlib.decompress(binascii.a2b_base64(binascii.a2b_qp(zlib.decompress(read_lock)))))))))))))))).splitlines() ]:
            self.__dict__[name] = eval(value)