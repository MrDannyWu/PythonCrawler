
'''
author：DannyWu
site:   www.idannywu.com
'''
from cities import cities

key = input("亲输入城市名称：")
try:
    city_code = cities[key]
    print(city_code)
except KeyError:
    print("此城市不存在！",KeyError)
