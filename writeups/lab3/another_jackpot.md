# Challenge `Another Jackpot` writeup

- **Vulnerability:** Race condition in `/login` endpoint
- **Where:** between associating a username to a cookie session and check if the parameters for login are valid.
- **Impact:** Allows accessing `/jackpot` endpoint without having admin's account password. Enables bypass of login authentication.

## Steps to reproduce

1. Create a new session or copy a valid cookie token value and set it constant for the following requests.
1. Make a POST request to `/login` endpoint with the "username" parameter with "admin" as value and a "password" parameter with an arbitrary value.
1. At the same time (concurrently), perform a GET request to `/jackpot`.
1. Repeat until the server acts as if you are logged in as admin and the GET request returns the flag.

[POC](another_jackpot.py)
