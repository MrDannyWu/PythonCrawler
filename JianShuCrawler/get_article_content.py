'''
author：DannyWu
site:   www.idannywu.com
'''

import requests
from bs4 import BeautifulSoup
#import pandas

header = {
    'Cookie': 'sajssdk_2015_cross_new_user=1; remember_user_token=W1s5ODQwNzBdLCIkMmEkMTAkWHg1VmhSeUN0Uj'
              'lkTU5MUGR4MlkvZSIsIjE1MzU2MzM5OTkuMTA2MTUxMyJd--40f6d0ec71d75a4074b66d8681b70b777bf6dc5b; '
              '_m7e_session=0deafbb3d670a21376a14c8ce9f7b47a; sensorsdata2015jssdkcross=%7B%22distinct_'
              'id%22%3A%22984070%22%2C%22%24device_id%22%3A%221658aeaea563d-0de0abf4c4010d-9393265-1049088'
              '-1658aeaea59167%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%'
              'E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_'
              'host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC'
              '_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221658aeaea563d-0de0abf4c40'
              '10d-9393265-1049088-1658aeaea59167%22%7D; read_mode=day; default_font=font1; locale=zh-CN;'
              ' Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1535634269; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9'
              'fb068=1535634269',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/68.0.3440.106 Safari/537.36',
}
url = "https://www.jianshu.com/search?q=%E5%8C%BA%E5%9D%97%E9%93%BE&page=101&type=note"
url1 = 'https://www.jianshu.com/p/381d7981888d'
url2 = 'https://www.jianshu.com/p/a166e63544d8'


def get_article_content(artile_url):
    web_data = requests.get(artile_url,headers=header)
    web_data.encoding = 'utf-8'
    #print(web_data)
    code = web_data.status_code
    if(code==200):
        soup = BeautifulSoup(web_data.text, 'lxml')
        titles = soup.select('body > div.note > div.post > div.article > h1')
        article_p = soup.select('p')
        content_free = soup.select('.show-content-free')
        article = []
        title = []
        if len(titles):
            #print(len(titles))
            print(titles[0].text)
            title.append(titles[0].text)
        else:
            print(len(titles))
            print('no data')
            pass
        #print(soup)
        #print(content_free)
        for cont in content_free:
            #print(cont)
            #print()
            article.append(cont.text)
        for p in article:
            print(p)
        data = {
            'article':'\n'.join(article),
            'title': title[0],
        }
        #df = pandas.DataFrame(data)
        #df.to_excel('jbook.xlsx')
        return data
    else:
        print("404 error")

#get_article_content(url2)
