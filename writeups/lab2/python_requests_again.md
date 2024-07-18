# Challenge `Python Requests Again` writeup

- **Vulnerability:** Vulnerable endpoint to brute-force and cookie manipulation.
- **Where:** `/more` endpoint and `remaining_tries` cookie value
- **Impact:** Number of allowed requests to the vulnerable endpoint can be arbitrarily modified which enables looping until the value matches the target.
- **NOTE:** Corrective measures implemented on top of previous challenge `Python Requests` but rendered ineffective by vulnerability.

## Steps to reproduce

1. Make an initial request by connecting to `/hello`. This is necessary to:
   - retrieve valid user token (cookies)
   - get target value
1. Modify the value of `remaining_tries` in the request cookie to an arbitrarily large number, effectively disabling the imposed corrective measure of maximum amount of consecutive tries.
1. Make continuously requests to `/more` until the current value matches the target value. (brute-force)
1. After the target value is achieved, connect to `/finish` and retrieve the flag.

[(POC)](pythonRequestsAgain.py)
