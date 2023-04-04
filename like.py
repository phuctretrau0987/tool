import threading
import requests
from pystyle import *
import time
import sys
import ssl
import random
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
import time
import os
import datetime
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context


class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False
    
class Main:
    def __init__(self, __file_name, __post):
        self.__success = 0
        self.__errors = 0
        self.rqs = 0
        self.rpm = 0
        self.rps = 0
        self.rqs = 0
        self.__post = __post
        self.__client = requests.Session()
        self.__client.cookies.set_policy(BlockCookies())
        try:
            self._file = open(__file_name).read().split('\n')
        except:
            sys.exit((f'[+] No Such File "{__file_name}"                                                                        '))
    def title(self, start):
        while True:
            curr_time = str(
                datetime.timedelta(
                    seconds = (
                        time.time() 
                        - start
                    )
                )
            ).split(".")[0]
            os.system(f'title Total: {str(len(self._file))} ^| Elapsed Time: {curr_time} ^| Success: {self.__success} ^| Fail: {self.__errors} ^| Cpm: {self.rpm} ^| Thread_Count: {threading.active_count()} ^| v2.1')
            time.sleep(0.5)
    
    def random_ico(self, length):
        icon = '🌁🌉🌌🌃🌆🌇🏙🎆🎇🌠🎑🌄🌅🏜🏞🌋🗻🏔⛰🗾⛺🏕🏝🏖🌼🌸🌺🏵️🌻🌷🌹🥀💐🌾🎋☘🍀🍃🍂🍁🌱🌿🎍🌵🌴🌳🌳🎄🍄🌜🌚❄🌪🌊☂️💦🌈🌩️🌥️⛅'
        result_ico = ''.join(random.choice(icon) for i in range(length))
        return result_ico

    def likes(self, token):
        __start = time.time()
        link = 'https://graph.facebook.com/'+self.__post+'/likes'
        data = {
                'access_token': token,
                }
        response = self.__client.post(link, data=data, verify=False, stream=False, allow_redirects=False).json()
        self.rqs += 1
        if True == response:
            print(f"[+] Likes! [{response}] [Execution: {round(time.time() - __start, 1)}s]")
            self.__success += 1
            time.sleep(0.05)
        else:
            self.__errors += 1
    def __share(self, token):
        self.likes(token)
        try:
            get_ = requests.get('https://graph.facebook.com/me/accounts?access_token='+token, verify=False, stream=False, allow_redirects=False).json()['data']
            for access in get_:
                tok = access['access_token']
                self.likes(tok)
        except:
             self.__errors += 1
    def rpsm_loop(self):
        while True:
            initial = self.rqs
            time.sleep(1.5)
            rps = round((self.rqs - initial) / 1.5, 1)
            self.rpm = round(rps * 60, 1)
    def start(self):
        threading.Thread(
                target = self.rpsm_loop, 
            ).start()
        threading.Thread(
                target = self.title, 
                daemon = True,
                args=[time.time()]
            ).start()
        for token in self._file:
            threading.Thread(target=self.__share, args=[token]).start()
            while threading.active_count() > 1000:
                pass
def run():
    __file = 'token.txt'
    __post = input("{?} Enter Post ID [Enter to start] -> ")
    Main(__file, __post).start()

if '__main__' == __name__:
    run()
