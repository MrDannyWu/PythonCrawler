from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
with open('citylist.xml','r',encoding='UTF-8') as r:
    xml = r.read()
    r.close()

soup = BeautifulSoup(xml,'lxml')
#print(soup.prettify())
city_info = soup.select('d')
for i in city_info:
    #print(i.get('d2'),' ',i.get('d1'))
    info = "'" + i.get('d2') + "'" + ":" + "'" + i.get('d1') + "'" + "," + "\n"
    with open('citylist.py','a') as f:
        f.write(info)

