# Challenge `Just my boring cookies` writeup

- **Vulnerability:** XSS
- **Where:** in search query
- **Impact:** Allows injection of \<script\> tag and execution of arbitrary script

## Steps to reproduce

1. Insert into search bar `<script>alert(document.cookie)</script>`
