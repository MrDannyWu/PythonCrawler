# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           161725.py
   Description:
   Author:        
   Create Date:    2021/03/30
-------------------------------------------------
   Modify:
                   2021/03/30:
-------------------------------------------------
"""
import requests
from lxml import etree
import pandas as pd

# url = 'http://www.cmfchina.com/servlet/fund/FundNavPageAction?numPerPage=8000&fundId=161725&startTime=2005-03-02&endTime=2021-03-30&flag=0&reqUrl=%2Fservlet%2Ffund%2FFundNavPageAction&_=1617092498395'
url = 'http://www.cmfchina.com/servlet/fund/FundNavPageAction?numPerPage=8000&fundId=161725'
resp = requests.get(url)

html = etree.HTML(resp.text)
tr_list = html.xpath('//tr')
total_data_list = []
for tr in tr_list[1:]:
    print(tr)
    td_list = tr.xpath('./td/text()')
    data_list = []
    for td in td_list:
        print(td.strip())
        data_list.append(td.strip())
    data_list.append(((float(td_list[2]) - 0.995)/0.995)* 100)
    total_data_list.append(data_list)


file_path = '../files/161725_2.xlsx'
columns = ['data', 'single_price', 'total_price', 'daily_rate', 'total_rate']
df = pd.DataFrame(total_data_list, columns=columns)
df.to_excel(file_path, index=False)