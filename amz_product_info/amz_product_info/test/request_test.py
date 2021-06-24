import requests

# url = 'https://httpbin.org/get'
url = 'https://www.amazon.com/XDOBO-Non-Slip-Pillows-Accessories-Reinforced/dp/B07RGN2TP9/'
header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6',
    'cookie': 'session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:CN"; session-id=136-5144459-7065013; ubid-main=132-5228167-2046518; x-wl-uid=10TwTcH7Zh+tDFXt9ni3fw+lwlyTng4Joqp9edQ/eC7OW0qOOzLc/SIw5AZkJY5Y7FSyMx6ld4wU=; session-token=u5y4XKIZyDmY3eIS5WzWddoxt6jRxQocm6suKeP6vf3LC+W9kIzgNW06kOZteZOT0i27DG8JTf6Yn+6oqVskMkn9GH2LMfdWrQnpI9wClz6zv3sH7g7yJeqh0liA+aTW06vrEaTjHnuwmmnO7EolV6h5pXqn+eeZS61YJPSaDgY6Mg5m3uYY50Zqve9cdbOb; x-amz-captcha-1=1571102337024506; x-amz-captcha-2=aaUuD+/t7jv2+Eyd2OtvfQ==; csm-hit=tb:SZ088R9F9ZEX58W0N8WA+s-P4RYFN7M00W34JNH1WPP|1571102721204&t:1571102721204&adb:adblk_no',
    'referer': 'https://www.amazon.com/XDOBO-Non-Slip-Pillows-Accessories-Reinforced/dp/B07RGN2TP9/',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
proxies = {
    'https': 'http://47.110.130.152:8080'
    # 'https': 'https://' + proxy,
}
resp = requests.get(url, headers=header, timeout=10, proxies=proxies)
print(resp.text)