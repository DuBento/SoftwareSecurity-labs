# Challenge `Simple Local Read` writeup

- **Vulnerability:** Format String
- **Where:** usage of printf() function
- **Impact:** Allows read arbitrary contents from stack

## Steps to reproduce

1. Send format string with `%s` until flag is printed.
1. Alternatively, determine stack contents with `%x` until flag address found, use `%s` to print flag.

[POC](simple_local_read.py)
