# Challenge `Return Address` writeup

- **Vulnerability:** Buffer Overflow ROP
- **Where:** buffer in challenge() written with gets()
- **Impact:** Allows writing over function return address and execute win() function

## Steps to reproduce

1. Get address of win function with `objdump -d` for example
1. Send input to fill the buffer and overwrite the stack up to the return address.
   ```
   win = b'\xf1\x86\x04\x08'
   msg = b'A'*22 + win
   ```
1. Challenge function will return to win() instead of main()

[POC](return_addr.py)
