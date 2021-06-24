import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
from db import *
from db_utils import *
from datetime import datetime
from multiprocessing import Pool


def save_email(connect, email, password, error, status):
    query_sql = 'select id from email where username="{}"'.format(email)
    results = query_results(connect, query_sql)
    print(results)
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if results[0] == 0:
        insert_sql = 'insert into email(username, password, error, status, createTime, updateTime)VALUES ("{}", "{}", "{}", "{}", "{}", "{}")'.format(email, password, error, status, create_time, update_time)
        insert_update_drop_data(connect, insert_sql, '成功插入！')
    # else:
    #     update_sql = 'update email set username="{}", password="{}", error="{}", status="{}", updateTime="{}"'


def auto_regist_email(ac):
    connect = connect_db(DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT)
    mail_login_url = 'https://mail.teekar.com/iredadmin'
    username = 'postmaster@teekar.com'
    password = 'Umiwe@520'
    cha_list = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    chrome_options = Options()
    # chrome_options.add_argument('blink-settings=imagesEnabled=false')
    # chrome_options.add_argument('--user-data-dir=D:\\ud')
    # # self.chrome_options.add_argument('--proxy-server=' +
    # # proxy.replace('https', 'http'))
    # chrome_options.add_argument('--proxy-server=http://10.11.2.251:3128')
    # chrome_options.add_argument('--proxy-server=http://183.129.244.16:17210')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--headless')
    #
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(mail_login_url)
    browser.find_element_by_id('user').send_keys(username)
    browser.find_element_by_id('password').send_keys(password)
    browser.find_element_by_css_selector('input.button.green').click()
    for i in range(2500):
        reg_name = ''.join(random.sample(cha_list, 9))
        reg_pass = '12344321'
        email_host = 'shoesyeah.com'
        email_address = reg_name + '@' + email_host
        # browser.get('https://mail.teekar.com/iredadmin/create/user/volbaby.com')
        browser.get('https://mail.teekar.com/iredadmin/create/user/shoesyeah.com')
        browser.find_element_by_xpath('//input[@name="username"]').send_keys(reg_name)
        browser.find_element_by_xpath('//input[@name="newpw"]').send_keys(reg_pass)
        browser.find_element_by_xpath('//input[@name="confirmpw"]').send_keys(reg_pass)
        browser.find_element_by_xpath('//input[@name="mailQuota"]').send_keys(2)
        browser.find_element_by_xpath('//input[@type="submit" and @value="Add"]').click()
        error = ''
        status = 0

        save_email(connect, email_address, reg_pass, error, status)
    time.sleep(10)
    browser.quit()


def main():

    pool = Pool(8)
    a_list = [x for x in range(8)]
    print(a_list)
    # for i in range(10000):
    #     a_list.append()
    # auto_regist_email(1)
    pool.map(auto_regist_email, a_list)
    pool.close()
    pool.join()
    # email = 'abcde'
    # password = ''
    # error = ''
    # status = 0
    # save_email(connect, email, password, error, status)
    # pass


if __name__ == '__main__':
    main()