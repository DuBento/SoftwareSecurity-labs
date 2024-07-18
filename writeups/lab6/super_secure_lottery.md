# Challenge `Super Secure Lottery` writeup

- **Vulnerability:** Buffer Overflow
- **Where:** buffer in run_lottery() written with read() [buffer size mismatch]
- **Impact:** Allows writing over local variables in the stack and bypass random match condition

## Steps to reproduce

1. Check where the random lottery value is stored with `gdb`
1. Send input to fill the buffer and overwrite the stack up to the lottery value.
   The first 8 bytes of this buffer will be used to match with the random token.
   We overwrite the random token with deterministic value (same as the first 8 bytes of our buffer)
   ebx register is necessary to access string and since address space randomization is deactivated we can check the value locally with gdb and add it to the buffer (maintains that value in the stack).
   'B' is used for filler.
   ```
   stack_base = b"\x08\xa0\x04\x08"
   msg = b'A'*8 + b'B'*8 + stack_base + b'B'*28 + b'A'*8
   ```
1. Memory compare function will return equal (0) since the memory has 'A'\*8 on both.

[POC](super_secure_lottery.py)
