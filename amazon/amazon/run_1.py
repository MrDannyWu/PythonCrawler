from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import logging
from scrapy.utils.project import get_project_settings
import random
import datetime
import time


# time.sleep(21660)
# 在控制台打印日志
configure_logging()
# CrawlerRunner获取settings.py里的设置信息
runner = CrawlerRunner(get_project_settings())


@defer.inlineCallbacks
def crawl():
    time_list = [120, 150, 160, 180, 200, 230, 250, 260, 60, 300, 100, 135, 271, 289]

    i = 0
    while True:
        now_time = datetime.datetime.now().strftime("%H")
        print(now_time)
        if '23' in now_time:
            reactor.stop()
            break
        time_sleep = random.choice(time_list)
        if i == 0:
            print('爬取目录和产品！')
            # yield runner.crawl('get_product_details')
            yield runner.crawl('get_category_product')
            print("time_sleep: " + str(time_sleep))
            time.sleep(time_sleep)
        if i == 1:
            print('第一次爬取产品详情！')
            # yield runner.crawl('get_product_details')
            yield runner.crawl('get_product_details')
            print("time_sleep: " + str(time_sleep))
            time.sleep(time_sleep)

        else:
            print("循环爬取产品详情开始!")
            logging.info("new cycle starting")
            yield runner.crawl('get_product_details_two')
            # 一分钟跑一次
            print("time_sleep: " + str(time_sleep))
            time.sleep(time_sleep)
        i += 1
    reactor.stop()


crawl()
# the script will block here until the last crawl call is finished
reactor.run()