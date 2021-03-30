# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           320007.py
   Description:    诺安成长混合
   Author:        
   Create Date:    2021/03/30
-------------------------------------------------
   Modify:
                   2021/03/30:
-------------------------------------------------
"""
import requests
import json
import pandas as pd

url = 'https://trade.lionfund.com.cn/pc/q/fundList!ajaxQueryFundHisNavDetail.action'
post_data = {
    'order': 0,
    'fundType': 3,
    'fundCode': 320007,
    'beginDate': 20000101,
    'endDate': 20210330
}

resp = requests.post(url, data=post_data)
json_data = json.loads(resp.text, encoding='utf-8')
print(json_data)
for i in json_data:
    print(i, ' --> ', json_data[i])
history_data = json_data['fundHisNavList']
data_list = []
count = []
for item in history_data:
    print(item)
    print(float(item['changeRate']))
    if float(item['changeRate']) > 0:
        count.append(item['changeRate'])
    data_list.append([item['priceDate'],item['priceDate1'][0:4] + '-' + item['priceDate1'][4:6] + '-' + item['priceDate1'][-2:],item['netValue'],item['totalNetValue'],item['changeRate'],item['performanceIndex']])

columns = ['priceDate', 'priceDate1', 'netValue', 'totalNetValue', 'changeRate', 'performanceIndex']

file_path = 'files/320007.xlsx'

print(len(data_list), len(count), len(data_list) - len(count))
df = pd.DataFrame(data_list, columns=columns)
df.to_excel(file_path, index=False)


