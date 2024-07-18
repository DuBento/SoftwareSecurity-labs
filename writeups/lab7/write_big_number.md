# Challenge `Write Big Number` writeup

- **Vulnerability:** Format String
- **Where:** usage of printf() function
- **Impact:** Allows arbitrary write in global variable

## Steps to reproduce

1. Determine global variable memory address using `gdb`, `nm` or python pwntools.
1. Craft a format string containing the addresses for each byte of the target variable.
1. For each byte define the padding needed to write that value using `%n`
1. Progressively write each byte's value by adjusting the padding (sometimes overflow is needed), %Y$hhn will write the number of characters printed to this point in that supplied byte address.

[POC](write_big_number.py.py)
