from pwn import *
import re

def web():
    r = remote('mustard.stt.rnl.tecnico.ulisboa.pt', 22055)
    
    ## parse initial
    initial_txt = r.recv().decode('utf8')
    print(initial_txt)
    match = re.findall(r'\d+', initial_txt)
    print(match)
    target = match[0]
    current = match[1]

    while True:
        r.sendline(b'MORE')
        txt = r.recv().decode('utf8')
        match = re.findall(r'\d+', txt)
        current = match[1]

        if current == target:
            break

    r.sendline(b'FINISH')
    print(r.recv())

web()

