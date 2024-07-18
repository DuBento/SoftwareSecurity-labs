# Challenge `Guess a BIG Number` writeup

- **Vulnerability:** Vulnerable endpoint to brute-force.
- **Where:** `/number/<guess>`
- **Impact:** Allows finding the correct number guess via binary search.

## Steps to reproduce

1. Start a python request session by connecting to the web server. This is necessary to:
   - retrieve valid user token (cookies)
   - get target value
2. Connect to `/number/<guess>` varying the guessed value _similar_ to a binary search algorithm:
   - Select a random number to start on.
   - If the feedback form received from the server indicates the value should be higher, then the new guess is the old value plus half of the difference between the two previous numbers:
     > number += (higher-lower)//2
   - if it should be lower, then the new guess is the old value minus half of the difference between the two previous numbers:
     > number -= (higher-lower)//2
3. When the target value is reached, the flag is printed.

[(POC)](bignumber.py)
