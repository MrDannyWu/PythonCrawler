import os
import time
import datetime
import platform


def run():
    # 获取平台标志
    platform_name = platform.architecture()[1].lower()

    # 在Windows平台下运行时：
    if 'windows' in platform_name:
        # Windows will be : (32bit, WindowsPE)
        print('程序开始在Windows平台下运行...')

        print('程序切换目录至D:/Workspace/python.system.com/Amz/get_sale_time')
        os.chdir('D:/Workspace/python.system.com/Amz/get_sale_time')

        num = 0
        while True:
            now_time = datetime.datetime.now().strftime("%H")
            print('现在是：' + now_time + '点')
            # if '03' in now_time:
            #     time.sleep(3600)
            # if '07' in now_time:
            #     time.sleep(3600)
            # if '11' in now_time:
            #     time.sleep(3600)
            # if '14' in now_time:
            #     time.sleep(3600)
            # if '18' in now_time:
            #     time.sleep(3600)
            # if '22' in now_time:
            #     time.sleep(1800)

            # if '23' in now_time:
            #     print('程序跳出！执行完毕！')
            #     break

            print('第{}次执行 get_product_sale_time'.format(num + 1))
            os.system('scrapy crawl get_product_sale_time')
            print('一共执行了{}次 get_product_sale_time'.format(num + 1))

            time.sleep(60)
            num += 1

    # 在 Linux平台下运行时：
    # elif 'elf' in platform_name:
    #     # Linux will be : (32bit, ELF)
    #     print('程序开始在Linux平台下运行...')
    #
    #     print('程序切换目录至/home/webapp/python.system.com/python.system.com/Amz/amazon/')
    #     os.chdir('/home/webapp/python.system.com/python.system.com/Amz/amazon/')
    #
    #     num = 0
    #     while True:
    #         now_time = datetime.datetime.now().strftime("%H")
    #         print('现在是：' + now_time + '点')
    #         if '03' in now_time:
    #             time.sleep(3600)
    #         if '07' in now_time:
    #             time.sleep(3600)
    #         if '11' in now_time:
    #             time.sleep(3600)
    #         if '14' in now_time:
    #             time.sleep(3600)
    #         if '18' in now_time:
    #             time.sleep(3600)
    #         if '22' in now_time:
    #             time.sleep(1800)
    #
    #         if '23' in now_time:
    #             print('程序跳出！执行完毕！')
    #             break
    #
    #         print('第{}次执行 get_product_details_two'.format(num + 1))
    #         os.system('scrapy crawl get_product_details_two')
    #         print('一共执行了{}次 get_product_details_two'.format(num + 1))
    #
    #         time.sleep(60)
    #         num += 1
    else:
        pass


def main():
    # print('已经开始了')
    # time.sleep(21660)
    run()


if __name__ == '__main__':
    main()
