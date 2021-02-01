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


def city_code_to_url(city_code):
    base_url = 'http://www.weather.com.cn/weather1d/{}.shtml'
    url = base_url.format(city_code)
    # print(url)
    return url


def pretty_print(trains,header):
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


def get_1day_weather_data(province, city_name, city_code, city_piny, web_data):
    try:
        soup = BeautifulSoup(web_data, 'lxml')
        datas = soup.select('script')
        address = soup.select('.ctop .crumbs')
        day_wea = soup.select('.t .clearfix .wea')[0].text
        night_wea = soup.select('.t .clearfix .wea')[1].text
        day_tem = soup.select('.t .clearfix .tem')[0].text.replace('\n', '')
        night_tem = soup.select('.t .clearfix .tem')[1].text.replace('\n', '')
        day_win = soup.select('.t .clearfix .win span')[0].get('title') + soup.select('.t .clearfix .win span')[0].text
        night_win = soup.select('.t .clearfix .win span')[1].get('title') + soup.select('.t .clearfix .win span')[1].text
        sun_up = soup.select('.t .clearfix .sunUp')[0].text.replace('\n', '')
        sun_down = soup.select('.t .clearfix .sunDown')[0].text.replace('\n', '')
        day_wea_list = [day_wea, day_tem, day_win, sun_up]
        night_wea_list = [night_wea, night_tem, night_win, sun_down]
        print(day_wea_list)
        print(night_wea_list)
        db_utils = DB_Utils()
        for data in datas:
            if 'hour3data' in str(data):
                data1 = {}
                data1 = data.text.split('=')[-1]
                # print(data1)
                data2 = json.loads(data1)
                # print(data2['1d'])
                print(address[0].text.replace('\n', '').replace(' ', ''), '实时天气：')
                city = address[0].text.replace('\n', '').replace(' ', '')
                # city_info = city + '实时天气：\n'
                data4 = []
                for i in data2['1d']:
                    data3 = [i.split(',')[0], i.split(',')[2], i.split(',')[3], i.split(',')[4], i.split(',')[5]]
                    print(data3)
                    data4.append(data3)
                weather_data_of_1day = {
                    'province': province,
                    'city_name': city_name,
                    'city_code': city_code,
                    'city_piny': city_piny,
                    'city': city,
                    'day_wea': day_wea_list,
                    'night_wea': night_wea_list,
                    '24hour_weather': data4
                    }
                db_utils.save_one_to_mongo('1day_weather_data', weather_data_of_1day)
                print('save to mongo')
    except:
        print(province, city_name, city_code)
        db_utils1 = DB_Utils()
        error_city ={
            'province': province,
            'city_name': city_name,
            'city_code': city_code,
        }
        db_utils1.save_one_to_mongo('error', error_city)
        print('save error to mongo')
        pass


if __name__ == "__main__":
    db_util = DB_Utils()
    db_util.drop_collection('1day_weather_data')
    data = db_util.query_all('citylist')
    for i in data:
        url = city_code_to_url(i.get('city_code'))
        province = i.get('province')
        city_name = i.get('city_name')
        city_code = i.get('city_code')
        city_piny = i.get('city_piny')
        info = [city_name, city_code, city_piny]
        print(info)
        web_data = get_weather_html(url)
        get_1day_weather_data(province, city_name, city_code, city_piny, web_data)

