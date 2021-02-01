import requests
from bs4 import BeautifulSoup


url = 'https://www.baidu.com/s?ie=utf-8&wd=python正则表达式'

header = {
        'Cookie':'BAIDUID=7222D846613C60B3A72A967FFC301358:FG=1; BIDUPSID=7222D846613C60B3A72A967FFC301358; PSTM=1540170752; BD_UPN=12314353; delPer=0; BD_HOME=0; H_PS_PSSID=1462_21108_27400_27376_26350_20718',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
        }
data = {
        'wd':'Python'
        }
res = requests.get(url,headers=header)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'lxml')
results = soup.select('.c-container h3')
time = soup.select('.m')
for i,j in zip(results,range(10)):
    print(i.text,j)
#print(res.text)
