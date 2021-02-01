'''
author : DannyWu
site   : www.idannywu.com
'''
import requests
from bs4 import BeautifulSoup
from citylist import cities
from prettytable import PrettyTable
import json
from db import DB_Utils
from lxml import etree

header = {
        'Cookie':'HttpOnly; UM_distinctid=1768a88bc2b8e8-0e9dfc7bae8d11-6d112d7c-1fa400-1768a88bc2c1039; CNZZDATA1278586242=1987685622-1608637768-%7C1608637768; CNZZDATA1278586243=439112825-1608638094-%7C1608638094; CNZZDATA1278535746=1558815721-1608638252-%7C1608638252; CNZZDATA1278536588=855627517-1608640202-%7C1608640202; CNZZDATA1278586248=1728915186-1608639913-%7C1608639913; CNZZDATA1278535754=201558252-1608638244-%7C1608638244; CNZZDATA1278566949=537565642-1608640244-%7C1608640244; CNZZDATA1278889522=854946263-1608638628-%7C1608638628; userNewsPort0=1; f_city=%E5%B9%BF%E5%B7%9E%7C101280101%7C; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1608641987; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1608641987; Wa_lvt_1=1608641987; Wa_lpvt_1=1608641987; HttpOnly',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }


def pretty_print(trains, header):
    pt = PrettyTable()
    pt._set_field_names(header)
    for train in trains:
        pt.add_row(train)
    print(pt)


def get_city_weather_url(city_name):
    base_url = 'http://www.weather.com.cn/weather1d/{}.shtml'
    for key in cities:
        if key == city_name:
            city_name = key
    print(city_name)
    try:
        city_code = cities[city_name]
        url = base_url.format(city_code)
        print(url)
        return url
    except:
        print('此城市城市不存在！')

def get_weather_html(url):
    try:
        web_data = requests.get(url)
        web_data.encoding = 'UTF-8'

        return web_data.text
    except:
        print('请求页面失败...')


def get_1day_weather_data(web_data):
    soup = BeautifulSoup(web_data, 'lxml')
    html = etree.HTML(web_data)
    # print(html)
    # print(soup)
    try:
        datas = html.xpath('//script')
        # print(datas)
        abc = soup.select('.ctop .crumbs')
        db_utils = DB_Utils()
        for data in datas:
            # print(data.text)
            # print(data.text())
            if 'hour3data' in str(data.text):
                print(data.text)
                data1 = {}
                # print('###########', data.text)
                data1 = data.text.split('=')[-1]
                # print('aaaa',data1)
                data2 = json.loads(data1)
                # print(data2['1d'])
                print(abc[0].text.replace('\n', '').replace(' ', ''), '实时天气：')
                city = abc[0].text.replace('\n', '').replace(' ', '')
                city_info = city + '实时天气：\n'
                data4 = []
                for i in data2['1d']:
                    # print(i.split(','))
                    #print(i.split(',')[0], end=' ')
                    # print(i.split(',')[1])
                    #print(i.split(',')[2], end=' ')
                    #print(i.split(',')[3], end=' ')
                    #print(i.split(',')[4], end=' ')
                    #print(i.split(',')[5])
                    data3 = [i.split(',')[0],i.split(',')[2] ,i.split(',')[3],i.split(',')[4],i.split(',')[5]]
                    print(data3)
                    data4.append(data3)
                weather_data = {
                        'city':city,
                        '24hour_weather':data4
                        }
                db_utils.save_one_to_mongo('24hour_weather',weather_data)
                print('save to mongo')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    db_util = DB_Utils()
    db_util.drop_collection('24hour_weather')
    web_data_list = []
    for key in cities:
        url = get_city_weather_url(key)
        web_data = get_weather_html(url)
        get_1day_weather_data(web_data)
        #web_data_list.append(web_data)

    #get_weather_data(web_data)
    #pool = Pool(1)
    #pool.map(get_1day_weather_data,web_data_list)
    #pool.close()


