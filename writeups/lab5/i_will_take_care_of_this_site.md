# Challenge `I will take care of this site` writeup

- **Vulnerability:** SQL injection
- **Where:** in login form
- **Impact:** Allows arbitrary login without knowing password. Special impact: it allows login as `admin`

## Steps to reproduce

1. As username for the login form use: `admin' --` and anything as the password.
