# Challenge `Secure by Design` writeup

- **Vulnerability:** Cookie manipulation.
- **Where:** `user` cookie value.
- **Impact:** Allows to login as any user, in this case the user "admin" is the target. Enables bypass of server side security measure that does not allow inserting "admin" as the username in the form.
- **Note:** Noticed by introducing "a" as the username and saw that the cookie value was short which suggests that the value depends on the introduced username. Additionally realized it was a base64 enconded value because of the "=" characters at the end which are used as padding in base64.

## Steps to reproduce

1. Make a GET request to the HTTP web server.
1. Alternatively:
   1. Using a tool like burpsuit: Intercept the request and change the cookie `user` value to "YWRtaW4=" which is "admin" enconded in base64.
   1. Change the cookie value directly in the browser developer tools.
1. The HTTP response contains the flag.
