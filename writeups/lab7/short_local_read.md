# Challenge `Short Local Read` writeup

- **Vulnerability:** Format String
- **Where:** usage of printf() function
- **Impact:** Allows read arbitrary contents from stack

## Steps to reproduce

1. Determine what is the position of the local variable. For example progressively loop through the values by using a positional argument `%n$x`. Need to use positional argument since input buffer is limited to 5.

[POC](short_local_read.py)
