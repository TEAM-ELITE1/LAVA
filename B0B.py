#!/data/data/com.termux/files/usr/bin/python

import platform,os,sys
print('\033[1;91m[\033[1;97m-\033[1;91m] \033[1;97m𝘾𝙃𝘼𝘾𝙆𝙄𝙉>')
bit = platform.architecture()[0]
if bit == '64bit':
    print(" [///] You Are 64 BIT USER")
    import LAVA64

elif bit == '32bit':
    print(" [///] You Are 32 BIT USER")
    import a32


