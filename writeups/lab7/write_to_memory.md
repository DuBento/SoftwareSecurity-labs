# Challenge `Write To Memomry` writeup

- **Vulnerability:** Format String
- **Where:** usage of printf() function
- **Impact:** Allows arbitrary write in global variable

## Steps to reproduce

1. Determine global variable memory address using `gdb` or `nm`.
1. Craft a string format with `@target%y$n` where y is the offset to where the buffer is in the stack since we need to access the "@target" part of our payload (address to write in). %n will write the number of characters written to the variable in that supplied address.

[POC](write_to_memory.py)
