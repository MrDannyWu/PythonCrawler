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

    print(pages_total)
    pages_link = []
    for i in range(pages_total):
        #print(url + str(i+1))
        #pic_detail_page = url + str(i+1)
        pages_link.append(url + str(i+1))
    return pages_link,pic_path


def download_pics(pic_page_url):
    #pic_path = create_save_folder(pic_page_url)
    header ={
        'cookie':'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1536981553; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1536986863',
        'referer': pic_page_url,
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    try:
        page_data = requests.get(pic_page_url,headers=header)
    #time.sleep(3)
    except:
        pass
    
    soup_data = BeautifulSoup(page_data.text,'lxml')
    img_link = soup_data.select('.main-image p a img')[0].get('src')
    print("img_link : ", img_link)
    pic_name = img_link.split('/')[-1]
    #print(pic_name)
    try:
        pic_data = requests.get(img_link,headers=header)
    except:
        pass
    #with open(str(pic_path) + "\\" + pic_name ,'wb') as f:
    with open( "mzitu\\"+pic_name ,'wb') as f:
        f.write(pic_data.content)
    #time.sleep(2)





#get_pics_for_one(aurl,header)


    

purl = 'http://www.mzitu.com/page/2/'
def get_pics_for_one_pages(url,header):
    web_data = requests.get(url,headers=header).text
    soup = BeautifulSoup(web_data,'lxml')
    pages_url = soup.select('#pins li span a')
    for page_url in pages_url:
        print(page_url.text)
        print(page_url.get('href'))
        url_list = get_pics_for_one(page_url.get('href')+"/")[0]
        pic_path = get_pics_for_one(page_url.get('href')+"/")[1]
        pool = Pool(10)
        pool.map(download_pics,url_list)



#get_pics_for_one_pages(purl,header)
if __name__ == '__main__':
    url1 = 'http://www.mzitu.com/page/2/'
    get_pics_for_one_pages(url1,header)





