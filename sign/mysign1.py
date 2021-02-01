import requests
from bs4 import BeautifulSoup

def create_sign(name):
    url = 'http://www.uustv.com/'
    form_data = {
        'word': name,
        'sizes': '60',
        'fonts': 'bzcs.ttf',
        'fontcolor': '#000000'
        }

    web_data = requests.post(url,data=form_data)
    web_data.encoding = 'utf-8'
    soup = BeautifulSoup(web_data.text,'lxml')
    tu = url + soup.select('.tu img')[0].get('src')
    img_res = requests.get(tu)
    with open(name+'.jpg','wb') as f:
        f.write(img_res.content)

def main():
    name = input("请输入您的名字(不超过三个汉字)：")
    create_sign(name)
    print("您的签名已完成，以图片的形式保存在当前目录！")

if __name__ == "__main__":
    main()
