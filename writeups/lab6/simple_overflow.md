# Challenge `Simple Overflow` writeup

- **Vulnerability:** Buffer Overflow
- **Where:** buffer in main written with gets()
- **Impact:** Allows writing over local variable `test`

## Steps to reproduce

1. Send input to fill the buffer plus new value for test variable.
   ```
   b'A'*128+b'\x01\x00\x00\x00'
   ```

[POC](simple_overflow.py)
