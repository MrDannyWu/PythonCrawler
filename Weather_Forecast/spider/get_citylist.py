'''
author : DannyWu
site   : www.idannywu.com
'''
import requests
from bs4 import BeautifulSoup
from db import DB_Utils
from config import CITYLIST_URL

#获取中国天气网的城市列表xml
def get_citylist_xml(url):
    try:
        web_data = requests.get(url)
        citylist_xml = web_data.text
        return citylist_xml
    except:
        print('获取城市列表请求失败...')


#使用BeautifulSoup解析列表xml并提取城市以及对应的城市代码构造一个城市列表字典
def get_citylist_to_txt(citylist_xml):
    soup = BeautifulSoup(citylist_xml,'lxml')
    #print(soup.prettify())
    city_info = soup.select('d')
    with open('citylist.py','a') as f:
        f.write('cities = {\n')
        f.close()
    for i in city_info:
        #print(i.get('d2'),' ',i.get('d1'))
        info = "\t"+"'" + i.get('d2') + "'" + ":" + "'" + i.get('d1') + "'" + "," + "\n"
        if i.get('d4') == '韩国':
            break
        with open('citylist.py','a') as f:
            f.write(info)
            f.close()
        print('正在写入城市列表：',i.get('d2'),'-',i.get('d4'))
    with open('citylist.py','a') as f:
        f.write('}')
        f.close()

#使用BeautifulSoup解析列表xml并提取城市信息存储到MongoDB
def get_citylist_to_mongo(citylist_xml):
    save_to_db = DB_Utils()
    soup = BeautifulSoup(citylist_xml,'lxml')
    #print(soup.prettify())
    city_info = soup.select('d')
    for i in city_info:
        data = {
                'province':i.get('d4'),
                'city_name':i.get('d2'),
                'city_code':i.get('d1'),
                'city_piny':i.get('d3')
                }
        if i.get('d4') == '韩国':
            break
        save_to_db.save_one_to_mongo('citylist',data)
        print('正在将城市列表存储到mongodb: #',i.get('d4'),i.get('d2'))



if __name__ == "__main__":
    #url = CITYLIST_URL
    db_utils = DB_Utils()
    db_utils.drop_collection('citylist')
    url = 'http://mobile.weather.com.cn/js/citylist.xml'
    citylist_xml = get_citylist_xml(url)
    get_citylist_to_mongo(citylist_xml)
