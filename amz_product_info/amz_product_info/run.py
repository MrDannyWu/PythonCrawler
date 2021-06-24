import os
import time
import datetime
import platform
import pymysql


# 正式环境数据库配置信息
DB_HOST = '192.168.109.68'
DB_USER = 'develop_user_main'
DB_PASS = '@WSXzaq1'
DATABASE = 'erp_collect'
DB_PORT = 3306

# 测试环境数据库配置信息
# DB_HOST = '192.168.109.21'
# DB_USER = 'root'
# DB_PASS = '!QAZxsw2'
# DATABASE = 'erp_collect'
# DB_PORT = 3306


def run():
    # 获取平台标志
    platform_name = platform.architecture()[1].lower()

    # 在Windows平台下运行时：
    if 'windows' in platform_name:
        # Windows will be : (32bit, WindowsPE)
        print('程序开始在Windows平台下运行...')

        date_today = datetime.datetime.now().strftime('%Y-%m-%d')
        connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
        cursor = connect.cursor()
        update_sql = 'update amz_product_url set error = "yes" where error = "no" and SUBSTR(update_time, 1,10) != "{}"'.format(date_today)
        cursor.execute(update_sql)
        connect.commit()

        print('执行 get_product_details')
        os.system('scrapy crawl get_product_details')

        num = 0
        while True:
            now_time = datetime.datetime.now().strftime("%H")
            print('现在是：' + now_time + '点')

            if '23' in now_time:
                print('程序跳出！执行完毕！')
                break

            time.sleep(60)
            print('第{}次执行 get_product_details_two'.format(num + 1))
            os.system('scrapy crawl get_product_details_two')
            print('一共执行了{}次 get_product_details_two'.format(num + 1))
            time.sleep(60)
            num += 1

    # 在 Linux平台下运行时：
    elif 'elf' in platform_name:
        # Linux will be : (32bit, ELF)
        print('程序开始在Linux平台下运行...')

        date_today = datetime.datetime.now().strftime('%Y-%m-%d')
        connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
        cursor = connect.cursor()
        update_sql = 'update amz_product_url set error = "yes" where error = "no" and SUBSTR(update_time, 1,10) != "{}"'.format(date_today)
        cursor.execute(update_sql)
        connect.commit()
        # update_sql = 'update amz_product set error = "no" where error = "yes"'

        print('执行 get_product_details')
        os.system('scrapy crawl get_product_details')

        time.sleep(60)

        num = 0
        while True:
            now_time = datetime.datetime.now().strftime("%H")
            print('现在是：' + now_time + '点')

            if '23' in now_time:
                print('程序跳出！执行完毕！')
                break

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
    #     # run()
    #     if '00' in now_time:
    #         run()
    run()


if __name__ == '__main__':
    main()
