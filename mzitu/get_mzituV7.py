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
from multiprocessing import Pool

aurl = 'http://www.mzitu.com/149482/'
header ={
        'cookie':'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1536981553; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1536986863',
        'referer': 'referer',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
        
        }

def get_pics_for_one(url):
    header ={
        'cookie':'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1536981553; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1536986863',
        'referer': url,
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
        }
    #browser = webdriver.Chrome()
    current_folder_path = os.getcwd()
    #print(current_folder_path)
    folder_path = str(current_folder_path) + '\\mzitu'
    
    path_is_exist = Path(folder_path)
    pages_link = []
    if path_is_exist.exists():
        pass
    else:
        path_is_exist.mkdir()

    try:
        web_data = requests.get(url,headers=header)

        soup = BeautifulSoup(web_data.text,'lxml')
        title = soup.select('.main-title')[0].text
        save_path = str(folder_path) + '\\' + title
        print("美图保存于：",save_path)
        pages_total = int(soup.select('.pagenavi a span')[-2].text)
        print("此美女图片总数：",pages_total)
        for i in range(pages_total):
        #print(url + str(i+1))
        #pic_detail_page = url + str(i+1)
            pages_link.append(url + str(i+1))
    except:
        pass
    return pages_link


def download_pics(pic_page_url):
    header ={
        'cookie':'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1536981553; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1536986863',
        'referer': pic_page_url,
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    try:
        page_data = requests.get(pic_page_url,headers=header)
        soup_data = BeautifulSoup(page_data.text,'lxml')
        img_link = soup_data.select('.main-image p a img')[0].get('src')
        img_alt = soup_data.select('.main-image p a img')[0].get('alt')
        print("img_link : ", img_link)
        pic_name = img_link.split('/')[-1]
        pic_save_path = "mzitu\\"+img_alt+"\\"
        path = Path(pic_save_path)
        #print(pic_save_path)
        #print(path)
        if path.exists():
            pass
        else:
            path.mkdir()
    #time.sleep(3)
    except:
        pass
    try:
        pic_data = requests.get(img_link,headers=header)
    except:
        pass
    #with open(str(pic_path) + "\\" + pic_name ,'wb') as f:
    try:
        if os.path.isfile(str(pic_save_path)+pic_name):
            print("########此图已经下载########")
        else:
            with open( str(pic_save_path)+pic_name ,'wb') as f:
                f.write(pic_data.content)
    except:
        pass
    #time.sleep(2)

def get_pics_for_one_pages(url,header,pool_num):
    try:
        web_data = requests.get(url,headers=header).text
        soup = BeautifulSoup(web_data,'lxml')
        pages_url = soup.select('#pins li span a')
        for page_url in pages_url:
            print('===============开始下载：',page_url.text+"==============")
            print("此美女美图链接",page_url.get('href'))
            url_list = get_pics_for_one(page_url.get('href')+"/")
            #pic_path = get_pics_for_one(page_url.get('href')+"/")[1]
            pool = Pool(pool_num)
            pool.map(download_pics,url_list)
            print("======================下载完成======================")
            print("")
    except:
        pass



#get_pics_for_one_pages(purl,header)
if __name__ == '__main__':
    print("                     |--------------------------------- |")
    print("                     | 欢迎使用无界面多线程美图下载器！ |")
    print("                     |       目标站点：mzitu.com        |")
    print("                     | 作者:DannyWu(mydannywu@gmail.com)|")
    print("                     | 博客站点：www.idannywu.com       |")
    print("                     | 此项目只供个人学习使用，请勿用于 |")
    print("                     |       其他商业用途，谢谢！       |")
    print("                     |       如若侵权，联系立删！       |")
    print("                     |----------------------------------|")
    page_num = int(input('请输入下载的页数：'))
    pool_num = int(input('请输入启动线程数: '))
    #print(type(page_num))
    #print(type(pool_num))
    print("                                美图下载器开始运行...           ")
    try:
        base_url = 'http://www.mzitu.com/page/{}/'
        start = "################第 {} 页开始################"
        end = "################第 {} 页结束################"
        for i in range(page_num):
            print(start.format(i+1))
            url = base_url.format(i+1)
            get_pics_for_one_pages(url,header,pool_num)
            print(end.format(i+1))
    except:
        pass
    print("")
    print("##################全部下载完成!##################")

