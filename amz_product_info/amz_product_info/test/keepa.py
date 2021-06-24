from amazon.db import DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime


def query_product():
    """
    查询数据库所有error不为404的产品
    :return: 返回查询结果
    """
    connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
    cursor = connect.cursor()
    # query_all_sql = 'select * from product where class_id = 6768 and asin = "B004O290TW"'
    query_all_sql = 'select * from amz_product where error != "404"'
    cursor.execute(query_all_sql)
    results = cursor.fetchall()
    return results


def get_days(browser, asin):
    base_url = 'https://keepa.com/iframe_addon.html#1-0-{}'
    url = base_url.format(asin)
    # browser = webdriver.Chrome()
    days = ''
    try:
        browser.get(url)
        time.sleep(5)
        # tag = browser.find_element_by_id('priceHistory')
        rank_days = browser.find_elements_by_class_name('legendRange')[-1]
        # print(rank_days.text)
        days = rank_days.text.split('(')[1].split('days')[0].strip()
    except:
        # print('没有此Asin值或请求失败！')
        days = ''
    # print(browser.page_source)
    return days


def main():
    chrome_options = Options()
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(chrome_options=chrome_options)

    results = query_product()
    for i in results:
        asin = i[2]
        days = get_days(browser, asin)
        if days != '':
            print(days)
        else:
            print('没有此Asin值或请求失败！')
        # time.sleep(1)
    browser.quit()


if __name__ == '__main__':
    main()
