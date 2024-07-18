# Challenge `I challenge you for a race` writeup

- **Vulnerability:** Race condition on program with higher permissions
- **Where:** between checking file access permissions and reading the file
- **Impact:** Allows reading files that our user does not have access to. In the case of the challenge, a `flag` file containing the flag and own by the user root.
- **Note:** Our user has write access to /tmp.

## Steps to reproduce

1. Create a file in `/tmp` directory, "/tmp/dummy" making sure the user has read access to the created file.
1. Create a soft link to that file `ln -s /tmp/dummy /tmp/sl`.
1. Execute the program "challenge" and introduce the path to the soft link as the file name.
1. At the same time as the previous program is executing, override the previous soft link with a new one having the same name but pointing to `/challenge/flag`.
1. Perform this steps until able to read contents from `/challenge/flag`

[POC](i_challenge_you_for_a_race_script.sh)
