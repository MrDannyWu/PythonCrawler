import os
import time
import datetime
import platform
from requests import get
from json import loads


def run():
    # 获取平台标志
    platform_name = platform.architecture()[1].lower()
    # 在Windows平台下运行时：
    if 'windows' in platform_name:
        # Windows will be : (32bit, WindowsPE)
        print('程序开始在Windows平台下运行...')

        print('程序切换目录至D:/Workspace/python.system.com/Amz/amz_sale_monitoring/')
        os.chdir('D:/Workspace/python.system.com/Amz/amz_sale_monitoring/')
        num = 0
        while True:
            now_time = datetime.datetime.now().strftime("%H")
            print('现在是：' + now_time + '点')
            print('第{}次执行 sale_monitoring'.format(num + 1))
            os.system('scrapy crawl sale_monitoring')
            print('一共执行了{}次 sale_monitoring'.format(num + 1))
            print('休息20分钟！')
            time.sleep(1200)
            num += 1

    # 在 Linux平台下运行时：
    elif 'elf' in platform_name:
        # Linux will be : (32bit, ELF)
        print('程序开始在Linux平台下运行...')

        print('程序切换目录至/home/webapp/python.system.com/python.system.com/Amz/amz_sale_monitoring/')
        os.chdir('/home/webapp/python.system.com/python.system.com/Amz/amz_sale_monitoring/')
        num = 0
        while True:
            now_time = datetime.datetime.now().strftime("%H")
            print('现在是：' + now_time + '点')
            print('第{}次执行 sale_monitoring'.format(num + 1))
            os.system('scrapy crawl sale_monitoring')
            print('一共执行了{}次 sale_monitoring'.format(num + 1))
            print('休息20分钟！')
            time.sleep(1200)
            num += 1
    else:
        pass


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


def main():
    print('已经开始了')
    commit_ip()
    run()


if __name__ == '__main__':
    main()
