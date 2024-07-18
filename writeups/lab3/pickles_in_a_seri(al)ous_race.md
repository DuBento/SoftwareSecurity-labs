# Challenge `Pickles in a seri(al)ous race` writeup

- **Vulnerability:** Remote code execution and race condition.
- **Where:** Remote code execution in `pickle.load` and race condition in swapping writing modes. Program loads file contents directly with pickle library on read.
- **Impact:** Allows remote code execution on server side. Challenge specific impact: enables reading file `home/ctf/flag`
- **Note:** Relies on vulnerability in pickle that enables command execution on host system. Switching between writing modes demands cleaning all files in the user directory, but the server accepts concurrent sessions, so there is a race condition between deleting the files in one session and reading the file in another, which we can exploit.

## Steps to reproduce

1. Connect with a constant username for the different tries.
1. Select write file in "FREE" mode, which writes the payload directly to a file, and send the payload to be written, the `pickle.dump` of a pickle bomb that executes commands on the server's host.
1. At the same time (concurrently), read the file with the same file name in "CLASSY" mode which loads the file content with pickle library before sending as response to the client.
1. Repeat until race condition is met and server reads the file previously written containing a pickle bomb. You will know by checking the output of the read operation.

[POC](<pickles_in_a_seri(al)ous_race.py>)
