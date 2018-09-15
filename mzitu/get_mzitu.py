'''
author: DanyyWu
site:   www.idannywu.com
'''
import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
import time
import selenium
from selenium import webdriver

aurl = 'http://www.mzitu.com/149482/'
header ={
        'cookie':'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1536981553; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1536986863',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
        
        }

def get_pics_for_one(url,header):
    browser = webdriver.Chrome()
    current_folder_path = os.getcwd()
    print(current_folder_path)
    folder_path = str(current_folder_path) + '\\mzitu'
    print(folder_path)
    path_is_exist = Path(folder_path)
    if path_is_exist.exists():
        pass
    else:
        path_is_exist.mkdir()

    try:
        web_data = requests.get(url,headers=header)
    except:
        pass
    soup = BeautifulSoup(web_data.text,'lxml')
    title = soup.select('.main-title')[0].text
    pages_total = int(soup.select('.pagenavi a span')[-2].text)

    pic_path = str(folder_path) + "\\" + title
    pic_path_is_exist = Path(pic_path)
    if pic_path_is_exist.exists():
        pass
    else:
        try:
            pic_path_is_exist.mkdir()
        except:
            pass
    print(pic_path)
    

    #print(pages_total)
    for i in range(pages_total):
        #print(url + str(i+1))
        pic_detail_page = url + str(i+1)
        try:
            #page_data = requests.get(pic_detail_page,headers=header)
            browser.get(pic_detail_page)
            #if i == 1 :
                #browser.find_element_by_class_name('pagenavi')
            time.sleep(3)
            #print(browser.page_source)
        except:
            pass



        soup_data = BeautifulSoup(browser.page_source,'lxml')
        img_link = soup_data.select('.main-image p a img')[0].get('src')
        print("img_link : ", img_link)
        #pic_name = img_link.split('/')[-1]
        #print(pic_name)
        try:
            #pic_data = requests.get(img_link,headers=header)
            browser.get(img_link)
            time.sleep(3)
            pic_soup = BeautifulSoup(browser.page_source,'lxml')
            print(browser.page_source)
            img_dlink = soup.select('img')[0].get('src')
            print("img_dlink : ", img_dlink)
            pic_name = img_link.split('/')[-1]
            pic_data = requests.get(img_link)

        except:
            pass
        with open(str(pic_path) + "\\" + pic_name ,'wb') as f:
            f.write(pic_data.content)
        time.sleep(2)


#    for page in pages:
#        print(page.text)
    #print(soup)

#get_pics_for_one(aurl,header)
url1 = 'http://www.mzitu.com/150343/'
get_pics_for_one(url1,header)
