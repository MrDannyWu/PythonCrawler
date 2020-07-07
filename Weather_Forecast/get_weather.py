import requests
import selenium
from selenium import webdriver as wb
from bs4 import BeautifulSoup
from cities import cities
from prettytable import PrettyTable
def pretty_print(trains,header):
    #trains=[[11,12,13,14,15,16],[21,22,23,24,25,26],[31,32,33,34,35,36]]
    #trains = [[12,12,12,1212,2],[1,2,3,4,6],[6,5,4,3,7]]
    #header = [colum1,colum2,colum3,colum4,colum5]
    #print(header)
    pt=PrettyTable()
    pt._set_field_names(header)
    for train in trains:
        pt.add_row(train)
    print(pt)
#pretty_print('list1','list2','list3','list4','list5')


#url = 'http://www.weather.com.cn/weather1d/101220101.shtml'
#url = 'http://www.weather.com.cn/weather1d/101161206.shtml'
def get_city_weather_url(city_name):
    base_url = 'http://www.weather.com.cn/weather1d/{}.shtml'
    for key in cities:
        if key in city_name:
            city_name = key
        elif city_name in key:
            city_name = key
    print(city_name)
    try:
        city_code = cities[city_name]
        url = base_url.format(city_code)
        print(url)
        return url
    except:
        print('你输入的城市不存在！')

header = {
        'Cookie':'vjuids=4438bee9b.166809f026c.0.e55a83d533b4b; vjlast=1539756196.1539756196.30; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1539756197; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1539756197; userNewsPort0=1; f_city=%E5%85%AD%E5%AE%89%7C101221501%7C',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
        }
def get_weather_details(url):
    web_data = get_weather_html(url)
    #print(web_data)
    try:
        html = BeautifulSoup(web_data,'lxml')
        address = html.select('.ctop .crumbs a')
        abc = html.select('.ctop .crumbs')
        address1 = html.select('.ctop .crumbs span')
        times = html.select('#curve .time em')
        wpics = html.select('#curve .wpic div big')
        tems = html.select('#curve .tem em')
        winfs = html.select('#curve .winf em')
        winls = html.select('#curve .winl em')
        #print(abc)
        #print(times)

#        for time in times:
#            print(time.text)
#        for wpic in wpics:
#            print(wpic.get('title'))
#        for tem in tems:
#            print(tem.text)
#        for winf in winfs:
#            print(winf.text)
#        for winl in winls:
#            print(winl.text)
        #print(html)
    except:
        print('无内容...')
    list1 = []
    list2 = []
    #print(address[0].text,address[1].text,address1[-1].text+' 今日天气：')
    #print(address.text)
#    for i in address:
#        print(i.text,end=' ')
#    for j in address1:
#        print(j.text,end=' ')
 #   print(' 今日天气：')

    print('')
    print(abc[0].text.replace('\n','').replace(' ',''),'实时天气：')
    for time,wpic,tem,winf,winl in zip(times,wpics,tems,winfs,winls):
        #print(time.text,wpic.text,tem.text,winf.text,winl.text,end='\n')
        list1 = [time.text,wpic.get('title'),tem.text,winf.text,winl.text]
        
        list2.append(list1)
    #print(list1)
    #for i in list2:
    #    print(i)
    header = ['时间','天气','温度','风向','风级']
    pretty_print(list2,header)

    #print(curve)

def get_weather_html(url):
    browser = wb.PhantomJS()
    try:
        browser.get(url)
        web_data = browser.page_source
        return web_data
    except:
        print('请求页面失败...')


#get_weather_html(url)
key = input("亲输入城市名称：")
url = get_city_weather_url(key)
get_weather_details(url)
