# Challenge `PwnTools Sockets` writeup

- **Vulnerability:** Vulnerable server to brute-force.
- **Where:** `MORE` user option
- **Impact:** Allows several continuous uses of the `MORE` option until the value matches the target.
- **Note:** Similar to **Python Requests** challenge but using plain TCP socket instead of HTTP requests.

## Steps to reproduce

1. Connect to server using python pwntools `remote` function.
1. Parse the target value given by the initial connection.
1. Send `b"MORE\n"` continuously until the current value matches the target value. (brute-force)
1. After the target value is achieved, send the payload `b"FINISH\n"` and retrieve the flag.

[(POC)](pwntoolsSockets.py)
