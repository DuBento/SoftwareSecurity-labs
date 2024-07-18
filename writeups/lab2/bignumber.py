import requests
from random import randint

s = requests.Session()

baseurl = "http://mustard.stt.rnl.tecnico.ulisboa.pt:22052/"
s.get(baseurl)

first = randint(0,100000)
print(first)

number = first
lower = 0
higher = 100000
while True:
    print(number)
    r = s.get(f"{baseurl}/number/{number}")
    if "Higher" in r.text:
        lower = number
        number += (higher-lower)//2
    elif "Lower" in r.text:
        higher = number
        number -= (higher-lower)//2
    else:
        print(r.text)
        break

print(r)
print(r.content)
print(r.text)
