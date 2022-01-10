import time
import requests
from bs4 import BeautifulSoup
import json
from types import SimpleNamespace
import os

while True:
    #blochchain
    r = requests.get('http://192.168.1.4:8008/api/sia/getChainStatus')
    soup = BeautifulSoup(r.text, 'html.parser')
    y = str(soup)
    y = json.loads(y, object_hook=lambda d: SimpleNamespace(**d))

    #walletsurr
    r1 = requests.get('http://192.168.1.4:8008/api/sia/getWalletInfo')
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    y1 = str(soup1)
    y1 = json.loads(y1, object_hook=lambda d: SimpleNamespace(**d))

    try:
        if not y1.height == y.height:
            print("Service Down!1", time.asctime(time.localtime(time.time())))
            os.system('sudo systemctl restart handyhost')
            time.sleep(12)
            os.system('sudo systemctl restart handyhost')

        if y.synced is True:
            print("Success!", y.height)

    except:
        print("Service Down!2", time.asctime(time.localtime(time.time())))
        os.system('sudo systemctl restart handyhost')
        time.sleep(12)
        os.system('sudo systemctl restart handyhost')
    time.sleep(20)
