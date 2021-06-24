# -*- coding: utf-8 -*-
import random
from scrapy import signals
import base64
import pymysql
from amz_product_info.db import *
import requests
import json
from random import choice
from amz_product_info.db_utils import *


class AmazonSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class AmazonDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomProxyMiddleware(object):
    # 定义构造器，初始化要写入的文件
    # def __init__(self):
    #     self.proxy_list = []
    #     # 连接MySQL数据库
    #     self.connect = pymysql.connect(host=DB_HOST_2, user=DB_USER_2, password=DB_PASS_2, db=DATABASE_2, port=DB_PORT_2)
    #     print('proxxxxxxxxxxxx连接成功！')
    #     self.cursor = self.connect.cursor()

    def process_request(self, request, spider):
        proxy = None
        # ip_list = []
        # query_proxy_sql = 'select proxyIp from proxy where isActive = 1'
        # query_result = query_results(self.connect, query_proxy_sql)
        # if query_result[0] > 0:
        #     ip_tup = query_result[1]
        #
        #     for i in ip_tup:
        #         ip_list.append(i[0])
        #
        # if len(ip_list) == 0:
        #     pass
        # else:
        #     proxy = 'https://' + choice(ip_list)

        proxy = '192.168.103.251:3128'
        # proxy = '10.11.2.251:3128'
        print(proxy)
        request.meta['proxy'] = proxy


class ProxyMiddlewareDanny(object):
    # 定义构造器，初始化要写入的文件
    def __init__(self):
        self.proxy_list = []
        # 连接MySQL数据库
        self.connect = pymysql.connect(host=DB_HOST_1, user=DB_USER_1, password=DB_PASS_1, db=DATABASE_1, port=DB_PORT_1)
        print('proxxxxxxxxxxxx连接成功！')
        self.cursor = self.connect.cursor()

    def process_request(self, request, spider):
        query_sql = 'select * from proxies_pool where status="active"'
        self.cursor.execute(query_sql)
        results = self.cursor.fetchall()
        for i in results:
            self.proxy_list.append(i[1])
        # print(self.proxy_list)
        proxy = random.choice(self.proxy_list)
        # proxy = 'https://183.196.168.194:9000'
        print(proxy)
        request.meta['proxy'] = proxy
        # request.meta['proxy'] = '10.11.2.251:3128'


class AbuyunProxy(object):

    # 代理服务器
    proxyServer = "http-dyn.abuyun.com:9020"
    # 代理隧道验证信息
    proxyUser = "H07NF04YO04YU57D"
    proxyPass = "6CFC2A49238DAB80"
    # for Python2
    # proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)
    proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

    def process_request(self, request, spider):
        proxy_list = [
            'http://91.211.245.193:80',
            'http://60.9.1.80:80',
            'http://185.243.56.176:8080',
            'http://140.206.203.56:9999',
            'http://108.61.159.164:8080',
            'http://117.191.11.76:80',
            'http://85.10.197.9:3128',
            'http://120.210.219.73:80',
            'http://111.231.94.44:8888'
        ]
        resp = requests.get('http://127.0.0.1:5010/get/')
        json_data = json.loads(resp.text)
        proxy = json_data['proxy']
        print('#################:', proxy)
        # request.meta["proxy"] = '119.161.98.131:3128'
        request.meta["proxy"] = 'https://' + proxy
        # request.meta["proxy"] = 'http://' + proxy

