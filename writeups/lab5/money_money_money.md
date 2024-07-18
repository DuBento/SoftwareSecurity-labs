# Challenge `Money, money, money!` writeup

- **Vulnerability:** SQL injection
- **Where:** In profile bio, SQL update operation.
- **Impact:** Allows modifying token value that should be read only.

## Steps to reproduce

1. Submit value for bio: `bla', tokens=31145, bio='a` where token value is the one suggested in the profile page.
