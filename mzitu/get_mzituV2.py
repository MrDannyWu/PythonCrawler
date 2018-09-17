#!/usrbin/env python3
# coding: utf-8

import requests
import sys
import io
import re
import os
from bs4 import BeautifulSoup
from multiprocessing import Pool


def get_pic(url):
    # 传入一个起始图片页面url，获取其他的所有图片页面url，如下：
    #<a href="http://www.mzitu.com/98966/2"><span>2</span></a>
    #    print ("获取页面url完成，开始获取图片url并下载...")
    try:
        q = requests.get(url, headers=head).text
        title_R = (r'<h2.*title">(.*)</h2>')
        title = re.findall(title_R, q)[0]
        page_R = (r'<span>(..)</span>')
        max_page = re.findall(page_R, q)[0]
        # title是网页标题，可能含有特殊字符，需过滤
        title = re.sub(u'[\/:*?">|< 满]+', "#", title)
        #title = re.sub(r'[.]+',"？",title)
        return (title, max_page)
    except:
        pass

    


def change_dir(where):
    try:
        os.chdir(where)
    except:
        os.mkdir(where)
        os.chdir(where)
        print("创建并切换到目录'" + where + "'完成")
#    print ("切换目录到'"+where+"'完成")


def down(one, url):
    # 传入一个包含图片的页面url，获取里面的图片地址并下载到本地，如下：
    #<img src="http://i.meizitu.net/2017/07/30a01.jpg" alt="**************">
    try:
        title = one[0]
        max_page = one[1]
        R = (r'<img src="(.*)" alt=".*>')
        change_dir('./mzitu')
    except:
        pass
    try:
        os.chdir("./" + title)
        print("'" + title + "'已下载，跳过")
        change_dir("../../")
    except:
        try:
            change_dir("./" + title)
            for i in range(0, int(max_page)):
                page = url + "/" + str(i + 1)
                html = requests.get(page, headers=head).text
                img_url = re.findall(R, html)[0]
                pic = requests.get(img_url, headers=head)
                with open(str(i) + '.jpg', 'wb') as f:
                    for p in pic:
                        f.write(p)
            change_dir("../../")
        except:
            pass


def get_url_list(url):
    # 传入all页面的url，获取其他的所有文章链接，如下：
    #<a href="http://www.mzitu.com/99009" target="_blank">********</a>
    text = requests.get(url).text
    R = (r'.*(http://www.mzitu.com/[0-9]+)".*')
#    print (text)
    print("从" + url + "获取专辑列表完成，开始获取页面url...")
    #for i in re.findall(R, text):
       # print(i)
    return re.findall(R, text)
#get_url_list('http://www.mzitu.com/all')

def get_pics_for_one_pages(url):
    web_data = requests.get(url).text
    soup = BeautifulSoup(web_data,'lxml')
    pages_url = soup.select('#pins li span a')
    urls = []
    for url in pages_url:
        url = url.get('href')
        urls.append(url)
    return urls


if __name__ == "__main__":
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码
    # 曾经在运行时报字符编码错误所以添加了一条，但是现在去掉了，貌似也没报错。。。
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Referer': 'http://www.mzitu.com/37288/3'}
    url = 'http://www.mzitu.com/all'
    #page_number = "2"
    #url_list = get_url_list(url)
    n = input('please enter pages: ')
    page_urls = 'http://www.mzitu.com/page/{}/'
    
    for i in range(int(n)):
        url_page = page_urls.format(i+1)
        url_list = get_pics_for_one_pages(url_page)
        print(url_list)
        
        for i in url_list:
            one = get_pic(i)
            down(one, i)
            print(i + "：已经全部下载完成")
