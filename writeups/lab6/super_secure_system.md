# Challenge `Super Secure System` writeup

- **Vulnerability:** Buffer Overflow ROP
- **Where:** buffer in check_password() written with strcpy()
- **Impact:** Allows writing over function return address and bypass if condition

## Steps to reproduce

1. Get address of instruction that prints flag with `gdb` for example
1. Send input to fill the buffer and overwrite the stack up to the return address. The return value will be the instruction inside the if.
   ebx register is necessary to access string and since address space randomization is deactivated we can check the value locally with gdb and add it to the buffer. We offset the value because strcpy will stop in \x00 if present in string
   ```
   stack_base = b"\x08\xa0\x04\x08"*2+b"\x08\xd0\xff\xff"
   win = b'\xd9\x87\x04\x08'
   msg = b'A'*(32) + stack_base + win
   ```
1. Challenge function will return to instruct inside if

[POC](super_secure_system.py)
