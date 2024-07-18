# Challenge `Python Requests` writeup

- **Vulnerability:** Vulnerable endpoint to brute-force.
- **Where:** `/more`
- **Impact:** Allows several continuous requests to the vulnerable endpoint until the value matches the target.

## Steps to reproduce

1. Start a python request session by connecting to `/hello`. This is necessary to:
   - retrieve valid user token (cookies)
   - get target value
2. Make continuously requests to `/more` until the current value matches the target value. (brute-force)
3. After the target value is achieved, connect to `/finish` and retrieve the flag.

[(POC)](pythonRequests.py)
