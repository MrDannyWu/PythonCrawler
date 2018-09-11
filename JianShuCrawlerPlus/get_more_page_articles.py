'''
author：DannyWu
site:   www.idannywu.com
'''

import requests
#from bs4 import BeautifulSoup
import json
from selenium import webdriver
import time
from get_article_contents import get_article_content
#import pandas
#import PhantomJS

url = 'https://www.jianshu.com'

def get_one_page_article(one_page_url):
    do = webdriver.ChromeOptions()
    do.add_argument(r'user-data-dir=C:\Users\DannyWu\AppData\Local\Google\Chrome\User Data')
    browser = webdriver.Chrome("chromedriver", 0, do)
    #browser = webdriver.Chrome()
    browser.get(one_page_url)
    #articles = []
    for i in range(4):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
        time.sleep(2)    
    for j in range(20):  
        try:
            button = browser.execute_script("var a = document.getElementsByClassName('load-more'); a[0].click();")
            #time.sleep(2)
        except:
            pass

        titles = browser.find_elements_by_class_name("title")
        for title in titles[:len(titles) - 2]:

            if title == 'None':
                pass
            else:
                print(title.get_attribute('href'))
                article_url = title.get_attribute('href')
                get_article_content(article_url)
 
get_one_page_article(url)
