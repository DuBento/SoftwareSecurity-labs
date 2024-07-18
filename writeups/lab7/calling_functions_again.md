# Challenge `Write Given Number` writeup

- **Vulnerability:** Format String
- **Where:** usage of printf() function
- **Impact:** Allows arbitrary write in PLT

## Steps to reproduce

1. Determine address for Win function and Exit PLT entry using `gdb`, `nm` or python pwntools.
1. Craft a format string containing the addresses for each byte of the PLT entry.
1. For each byte define the padding needed to write that value using `%n`. The value we want to write is the address for the WIN function (to call that function instead of exit in GOT)
1. Progressively write each byte's value by adjusting the padding (sometimes overflow is needed) to match the received random value bytes, %Y$hhn will write the number of characters printed to this point in that supplied byte address.

[POC](calling_functions_again.py)
