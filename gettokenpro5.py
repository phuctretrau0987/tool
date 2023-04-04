import requests
stt = 0
_file = open('token.txt').read().split('\n')
for token in _file:
    try:
        get_ = requests.get('https://graph.facebook.com/me/accounts?access_token='+token).json()['data']
        for access in get_:
            stt += 1
            tok = access['access_token']
            print(f'[{stt} {access["name"]} | {tok}')
            with open("token-pageprofile.txt", "a+") as f:
                f.write(tok+'\n')
    except:
      pass
input(f'GET SUCCESS => {stt} TOKEN!')