import requests
from bs4 import BeautifulSoup
from pathlib import Path
import os


header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
page_url = 'https://movie.douban.com/top250?start={}&filter='

def get_more_pages(page_url):
    for i in range(0,250,25):
        url = page_url.format(i)
        get_details(url, header)


def get_details(url,header):
    current_path = os.getcwd();
    folder_path = current_path + "\\douban"
    path = Path(folder_path)
    web_data = requests.get(url,headers = header)
    soup = BeautifulSoup(web_data.text, 'lxml')
    imgs = soup.select('img')[:-1]
    if (path.exists()):
        pass
    else:
        path.mkdir()
    for img in imgs:
        name = img.get('alt')
        img_download_link = img.get('src')
        pic_name = name + '.' + img_download_link.split('.')[-1]
        res = requests.get(img_download_link)
        with open(str(path) + "\\" + pic_name, 'wb') as f:
            f.write(res.content)
        print(name)

if __name__ == "__main__":
    get_more_pages(page_url)
