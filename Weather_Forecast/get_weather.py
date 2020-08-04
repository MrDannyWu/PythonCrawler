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

header = {
        'Cookie':'vjuids=4438bee9b.166809f026c.0.e55a83d533b4b; vjlast=1539756196.1539756196.30; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1539756197; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1539756197; userNewsPort0=1; f_city=%E5%85%AD%E5%AE%89%7C101221501%7C',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
        }

def pretty_print(trains,header):
    pt=PrettyTable()
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
    datas = soup.select('script')
    abc = soup.select('.ctop .crumbs')
    db_utils = DB_Utils()
    for data in datas:
        if 'hour3data' in str(data):
            data1 = {}
            data1 = data.text.split('=')[-1]
            # print(data1)
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


