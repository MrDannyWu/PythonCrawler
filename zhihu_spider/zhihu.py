import requests

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument('blink-settings=imagesEnabled=false')
# self.chrome_options.add_argument('--disable-gpu')
# self.chrome_options.add_argument('--headless')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

chrome = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://www.zhihu.com/search?type=content&q=%E6%88%91%E5%92%8C%E6%88%91%E7%9A%84%E5%AE%B6'
chrome.get(url)

cookie_list = [
{
    "domain": ".zhihu.com",
    "expirationDate": 1664678988,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_ga",
    "path": "/",

    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "GA1.2.1032964337.1588870106",
    "id": 1
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1601607038,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_gat_gtag_UA_149949619_1",
    "path": "/",

    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1",
    "id": 2
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1601693388,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_gid",
    "path": "/",

    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "GA1.2.1350768212.1601605957",
    "id": 3
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1667087406.198433,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_xsrf",
    "path": "/",

    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "CgrEHGsPWv2lm9ipWE3bWpU3ZXwo1wmp",
    "id": 4
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1651942104.93371,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_zap",
    "path": "/",

    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "ceb80b78-e15b-455b-bdba-3c56f9f7ae65",
    "id": 5
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1604198977.466728,
    "hostOnly": False,
    "httpOnly": True,
    "name": "capsion_ticket",
    "path": "/",

    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "\"2|1:0|10:1601606978|14:capsion_ticket|44:NmEzZTFhZmZlYWI1NDk5Nzk1OWM1OTI0YzM4Yjg1N2I=|55fa73dd8e8f7f7a03228e2107d8db8261d22e5ab21199aa6d8aa7c2d778dc33\"",
    "id": 6
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1683478104.933775,
    "hostOnly": False,
    "httpOnly": False,
    "name": "d_c0",
    "path": "/",

    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "\"AICdjx0WPBGPTqB0vuS-iQYo1pylSptOHsU=|1588870105\"",
    "id": 7
},
{
    "domain": ".zhihu.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49",
    "path": "/",

    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "1601606988",
    "id": 8
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1633142988,
    "hostOnly": False,
    "httpOnly": False,
    "name": "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49",
    "path": "/",

    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1601605957,1601605965,1601606847",
    "id": 9
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1601608717.871449,
    "hostOnly": False,
    "httpOnly": False,
    "name": "unlock_ticket",
    "path": "/",

    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "\"ABCKT_K9nwgmAAAAYAJVTUqcdl94Lx15cbaIAfEF5uiOdTCB2D55Wg==\"",
    "id": 10
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1617158977.871398,
    "hostOnly": False,
    "httpOnly": True,
    "name": "z_c0",
    "path": "/",

    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "\"2|1:0|10:1601606978|4:z_c0|92:Mi4xeGJjSkFnQUFBQUFBZ0oyUEhSWThFU1lBQUFCZ0FsVk5RdU5qWUFDUEpSeE9VbUlJMG9iVkUxS3FaNzZJdzByaFd3|690e0554d450679c89fe867f15fda8f3b1f22e9e6b211061cf069d64b47c5a64\"",
    "id": 11
},
{
    "domain": "www.zhihu.com",
    "hostOnly": True,
    "httpOnly": False,
    "name": "JOID",
    "path": "/",

    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "U1oUA0vStRauttklENO3BWs-Bd4Bt_pZ2vWTbnSd50zc0pJtW5QmYfC02ScRDoY4O9Cv9Sdva4EWYYGjQh8Oe78=",
    "id": 12
},
{
    "domain": "www.zhihu.com",
    "hostOnly": True,
    "httpOnly": False,
    "name": "KLBRSID",
    "path": "/",

    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "d017ffedd50a8c265f0e648afe355952|1601606990|1601605956",
    "id": 13
},
{
    "domain": "www.zhihu.com",
    "hostOnly": True,
    "httpOnly": False,
    "name": "osd",
    "path": "/",

    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "W1AQAkjavxKvtdEvFNK0DWE6BN0Jvf5Y2f2ZanWe70bY05FlUZAnYvi-3SYSBow8OtOn_yNuaIkcZYCgShUKerw=",
    "id": 14
},
{
    "domain": "www.zhihu.com",
    "hostOnly": True,
    "httpOnly": False,
    "name": "SESSIONID",
    "path": "/",

    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "fLNtBIHeNQYsdJKHC6alsNSIDUbApM9kX49XXFumbS6",
    "id": 15
}
]
for i in cookie_list:
    chrome.add_cookie(i)

chrome.get(url)

time.sleep(10000)