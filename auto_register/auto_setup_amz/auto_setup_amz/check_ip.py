# -*- coding: utf-8 -*-
import requests

url = 'http://www.httpbin.org'

proxy = {
    'http': 'http://58.218.214.152:16349'
}
try:
    resp = requests.get(url, proxies=proxy)
    resp.encoding = 'utf-8'
    print(resp)
    # print(resp.text)
except Exception as e:
    print(e)


