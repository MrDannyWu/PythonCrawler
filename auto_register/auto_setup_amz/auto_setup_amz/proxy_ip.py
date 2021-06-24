'''
@Author: your name
@Date: 2019-12-18 09:07:14
@LastEditTime : 2020-01-04 11:20:35
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \auto_setup_amz\auto_setup_amz\proxy_ip.py
'''
# -*- coding: utf-8 -*-
from requests import get
from db_utils import insert_update_drop_data, connect_db, query_results
from db import *
from datetime import datetime, timedelta
from random import choice
from time import sleep
from json import loads


def save_ip(data, conn):

    now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for ip_text in data[1]:
        # ip_text = data[1]
        if ip_text != '':
            insert_sql = 'insert into proxy(proxyIp, isActive, updateTime) VALUES("{}", {}, "{}")'.format(ip_text, 1, now_time)
            print(insert_sql)
            insert_update_drop_data(conn, insert_sql, '')


def get_proxy_ip(url):
    try:
        if 'qingjuhe.cn' in url:
            resp = get(url)
            return resp, resp.text.split('*<-->*')
        elif '183.129.244.16' in url:
            resp = get(url)
            json_data = loads(resp.text)
            proxy_ip = json_data['domain'] + ':' + str(json_data['port'][0])
            print(proxy_ip)
            return resp, proxy_ip
    except Exception as e:
        print(e)
        return ''


# def commit_ip():
#     try:
#         resp_1 = get('https://jsonip.com/')
#         # resp = get('http://httpbin.org/ip')
#         # print(resp.text)
#         # json_data = loads(resp.text)
#         # origin_ip = json_data['origin'].split(',')[0]
#         json_data_1 = loads(resp_1.text)
#         origin_ip_1 = json_data_1['ip']
#         # print(origin_ip)
#         print(origin_ip_1)
#         get('http://ty-http-d.upupfile.com/index/white/add?neek=tyhttp802165&appkey=f33f8c574ddbc7ab2d517cdc0343f9d4&white={}'.format(origin_ip_1))
#         # print('本机外网IP为：', origin_ip)
#     except Exception as e:
#         print(e)

def commit_ip():
    try:
        # resp_1 = get('https://jsonip.com/')
        resp = get('http://httpbin.org/ip')
        # print(resp.text)
        json_data = loads(resp.text)
        origin_ip = json_data['origin'].split(',')[0]
        # json_data_1 = loads(resp_1.text)
        # origin_ip_1 = json_data_1['ip']
        print(origin_ip)
        # print(origin_ip_1)
        get('http://ty-http-d.upupfile.com/index/white/add?neek=tyhttp802165&appkey=f33f8c574ddbc7ab2d517cdc0343f9d4&white={}'.format(origin_ip))
        # print('本机外网IP为：', origin_ip)
    except Exception as e:
        print(e)


if __name__ == '__main__':


    while True:
        try:
            commit_ip()
            pre_time = (datetime.now() - timedelta(minutes=0)).strftime('%Y-%m-%d %H:%M:%S')
            connect = connect_db(DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT)
            update_sql = 'update proxy set isActive = 0 where updateTime < "{}"'.format(pre_time)
            insert_update_drop_data(connect, update_sql, '')
            # url = 'http://http.tiqu.qingjuhe.cn/getip3?num=1&type=1&pack=43560&port=11&yys=100017&lb=1&pb=45&gm=4&regions='
            # url = 'http://183.129.244.16:88/open?user_name=dfbhrehtp1&timestamp=1576810228&md5=53D0A64BB6C69B9C0442827DBEE4188E&pattern=json&number=1'
            # url = 'http://http.tiqu.qingjuhe.cn/getip3?num=1&type=1&pack=43545&port=1&yys=100017&lb=1&pb=45&gm=4&regions='
            # url = 'http://http.tiqu.qingjuhe.cn/getip3?num=3&type=1&pack=44015&port=1&yys=100017&lb=6&sb=%2A%3C--%3E%2A&pb=45&gm=4&regions='
            # url = 'http://http.tiqu.qingjuhe.cn/getip3?num=3&type=1&pack=44015&port=1&lb=6&sb=%2A%3C--%3E%2A&pb=45&gm=4&regions='
            url_1 = 'http://http.tiqu.qingjuhe.cn/getip3?num=3&type=1&pack=45255&port=11&lb=6&sb=%2A%3C--%3E%2A&pb=45&gm=4&regions='
            # result = get_proxy_ip(url)
            # if result == '':
            #     pass
            # else:
            #     print(result)
            #     save_ip(result, connect)
            # sleep(1.5)
            result_1 = get_proxy_ip(url_1)
            if result_1 == '':
                pass
            else:
                print(result_1)
                save_ip(result_1, connect)

            print('休息三分钟！')
            sleep(180)
        except:
            pass
    #
    # connect = connect_db(DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT)
    # # update_sql = 'update proxy set isActive = 0'
    # query_proxy_sql = 'select proxyIp from proxy where isActive = 1'
    # query_result = query_results(connect, query_proxy_sql)
    # ip_tup = query_result[1]
    # ip_list = []
    # for i in ip_tup:
    #     ip_list.append(i[0])
    # print(ip_list)
    # if len(ip_list) == 0:
    #     pass
    # else:
    #     proxy = choice(ip_list)
    #
    # print(proxy)
