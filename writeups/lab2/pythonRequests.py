# SSof{Python_requests_is_a_good_complement_to_ZAP}
import requests

s = requests.Session()

baseurl = "http://mustard.stt.rnl.tecnico.ulisboa.pt:22053"
r = s.get(f'{baseurl}/hello')

while True:
    r = s.get(f'{baseurl}/more')
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
r = s.get(f'{baseurl}/finish')
print(r.text)
