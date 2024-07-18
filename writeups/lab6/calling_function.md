# Challenge `Calling Function` writeup

- **Vulnerability:** Buffer Overflow
- **Where:** buffer in main() written with gets()
- **Impact:** Allows writing over local variable (function point) and execute win() function

## Steps to reproduce

1. Get address of win function with `objdump -d` for example
1. Send input to fill the buffer plus the address of win() to overwrite fp.
   ```
   win = b'\xf1\x86\x04\x08'
   msg = b'A'*32+win
   ```
1. Main function will call win()

[POC](calling_func.py)
