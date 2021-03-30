# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           csv_to_excel.py
   Description:
   Author:        
   Create Date:    2020/11/18
-------------------------------------------------
   Modify:
                   2020/11/18:
-------------------------------------------------
"""
import time
import pandas as pd

def csv_to_excel_fun(file_name):
    csv_file_name = file_name.replace('\\', '/').replace('"', '')
    print('原始csv路径：', csv_file_name)
    df = pd.read_csv(csv_file_name, low_memory=False)
    excel_file_name = csv_file_name.replace('.csv', '.xlsx')
    print('转换后的excel路径：', excel_file_name)
    df.to_excel(excel_file_name, index=False)


if __name__ == '__main__':
    while True:
        csv_file = input('请输入要解密的csv文件路径: ')
        start_time = time.time()
        csv_to_excel_fun(csv_file)
        end_time = time.time()
        duration = end_time - start_time
        print_text = 'CSV to EXCEL 转换完成！一共用时：{} 秒'.format(duration)
        print(print_text)