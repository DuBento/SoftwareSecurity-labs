# Challenge `Write Specific Value` writeup

- **Vulnerability:** Format String
- **Where:** usage of printf() function
- **Impact:** Allows arbitrary write in global variable

## Steps to reproduce

1. Determine global variable memory address using `gdb`, `nm` or python pwntools.
1. Craft a string format with `@target%0Zx%Y$n` where Z is the difference between what is already printed and a padding needed to meet 68 (which is the target value).Y is the offset to where the buffer is in the stack since we need to access the "@target" part of our payload (address to write in). %n will write the number of characters written to the variable in that supplied address.

[POC](write_specific_value.py)
