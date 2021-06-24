import os
import time
import datetime
import platform
# from amazon.db import DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT
import pymysql


# 正式环境数据库配置信息
DB_HOST = '10.11.2.68'
DB_USER = 'develop_user_danny'
DB_PASS = 'Aa123456!@#'
DATABASE = 'erp_collect'
DB_PORT = 3306

# 测试环境数据库配置信息
# DB_HOST = '10.11.2.21'
# DB_USER = 'root'
# DB_PASS = '!QAZxsw2'
# DATABASE = 'erp_collect'
# DB_PORT = 3306


def update_product():
    """
    每天第一次运行时将数据库产品表的is_new状态1全部变为状态0
    每天第一次运行时将数据库产品表的error状态no全部变为状态yes
    :return: None
    """
    try:
        connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
        cursor = connect.cursor()
        update_sql = 'update amz_product set is_new = 0 where is_new = 1'
        cursor.execute(update_sql)
        connect.commit()
        # update_sql = 'update amz_product set error = "no" where error = "yes"'
        print('更新成功！')
    except:
        pass


def run():
    # 获取平台标志
    platform_name = platform.architecture()[1].lower()

    # 在Windows平台下运行时：
    if 'windows' in platform_name:
        # Windows will be : (32bit, WindowsPE)
        print('程序开始在Windows平台下运行...')

        print('程序切换目录至D:/Workspace/python.system.com/Amz/amazon/')
        os.chdir('D:/Workspace/python.system.com/Amz/amazon/')

        print('开始抓取Top100的目录和产品')
        os.system('scrapy crawl get_category_product')
        print('抓取Top100的目录和产品已完成')

        date_today = datetime.datetime.now().strftime('%Y-%m-%d')
        connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
        cursor = connect.cursor()
        update_sql = 'update amz_product set error = "yes" where error = "no" and SUBSTR(update_time, 1,10) != "{}"'.format(date_today)
        cursor.execute(update_sql)
        connect.commit()
        # update_sql = 'update amz_product set error = "no" where error = "yes"'

        # print('开始第一次抓取产品详情')
        # os.system('scrapy crawl get_product_details')
        # print('第一次抓取产品详情已结束')

        num = 0
        while True:
            now_time = datetime.datetime.now().strftime("%H")
            print('现在是：' + now_time + '点')
            # if '03' in now_time:
            #     time.sleep(1800)
            # if '07' in now_time:
            #     time.sleep(1800)
            # if '11' in now_time:
            #     time.sleep(1800)
            # if '14' in now_time:
            #     time.sleep(1800)
            # if '18' in now_time:
            #     time.sleep(1800)
            # if '22' in now_time:
            #     time.sleep(1800)

            if '23' in now_time:
                print('程序跳出！执行完毕！')
                break

            print('第{}次执行 get_product_details_two'.format(num + 1))
            os.system('scrapy crawl get_product_details_two')
            print('一共执行了{}次 get_product_details_two'.format(num + 1))

            time.sleep(60)
            print('第{}次执行 get_product_details_three'.format(num + 1))
            os.system('scrapy crawl get_product_details_three')
            print('一共执行了{}次 get_product_details_three'.format(num + 1))
            time.sleep(60)
            num += 1

    # 在 Linux平台下运行时：
    elif 'elf' in platform_name:
        # Linux will be : (32bit, ELF)
        print('程序开始在Linux平台下运行...')

        print('程序切换目录至/home/webapp/python.system.com/python.system.com/Amz/amazon/')
        os.chdir('/home/webapp/python.system.com/python.system.com/Amz/amazon/')

        print('开始抓取Top100的目录和产品')
        os.system('scrapy crawl get_category_product')
        print('抓取Top100的目录和产品已完成')

        date_today = datetime.datetime.now().strftime('%Y-%m-%d')
        connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
        cursor = connect.cursor()
        update_sql = 'update amz_product set error = "yes" where error = "no" and SUBSTR(update_time, 1,10) != "{}"'.format(date_today)
        cursor.execute(update_sql)
        connect.commit()
        # update_sql = 'update amz_product set error = "no" where error = "yes"'

        # print('开始第一次抓取产品详情')
        # os.system('scrapy crawl get_product_details')
        # print('第一次抓取产品详情已结束')

        num = 0
        while True:
            now_time = datetime.datetime.now().strftime("%H")
            print('现在是：' + now_time + '点')
            # if '03' in now_time:
            #     time.sleep(1800)
            # if '07' in now_time:
            #     time.sleep(1800)
            # if '11' in now_time:
            #     time.sleep(1800)
            # if '14' in now_time:
            #     time.sleep(1800)
            # if '18' in now_time:
            #     time.sleep(1800)
            # if '22' in now_time:
            #     time.sleep(1800)

            if '23' in now_time:
                print('程序跳出！执行完毕！')
                break

            print('第{}次执行 get_product_details_three'.format(num + 1))
            os.system('scrapy crawl get_product_details_three')
            print('一共执行了{}次 get_product_details_three'.format(num + 1))

            time.sleep(60)
            print('第{}次执行 get_product_details_two'.format(num + 1))
            os.system('scrapy crawl get_product_details_two')
            print('一共执行了{}次 get_product_details_two'.format(num + 1))
            time.sleep(60)
            num += 1
    else:
        pass


def main():
    print('已经开始了')
    # while True:
    #     now_time = datetime.datetime.now().strftime("%H")
    #     print('现在是：' + now_time + '点')
    #     if '00' in now_time:
    #         update_product()
    #         run()
    update_product()
    run()


if __name__ == '__main__':
    main()
