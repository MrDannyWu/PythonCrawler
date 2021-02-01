'''
author : DannyWu
site   : www.idannywu.com
'''
from db import DB_Utils
from get_weather import *
db1 = DB_Utils()
arg = {'city_name':'蚌埠'}
result = db1.query_of_arg('1day_weather_data',arg)
header = ['1','2','3','4','5']
for i in result:
    #print(i)
    #print(i.get('24hour_weather'))
    print(i.get('city'))
    weather = [i.get('day_wea'),i.get('night_wea')]

    pretty_print(weather,['1','2','3','4'])
    print('24小时实时天气：')
    pretty_print(i.get('24hour_weather'),header)
#url = get_city_weather_url('蚌埠')
#web_data = get_weather_html(url)
#print(web_data)
#get_weather_data(web_data)
