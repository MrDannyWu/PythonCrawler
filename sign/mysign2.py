import requests
from bs4 import BeautifulSoup

def create_sign(name):
    url = 'http://www.jiqie.com/a/re19.php'
    form_data = {
        'id': name,
        'zhenbi': '20191123',
        'id1': '1605',
        'id2': '363',
        'id3':'#000000',
        'id4':'#FFF7D1',
        'id5':  -1
        }
    web_data = requests.post(url,data=form_data)
    web_data.encoding = 'utf-8'
    soup = BeautifulSoup(web_data.text,'lxml')
    tu = soup.select('img')[0].get('src')
    img_res = requests.get(tu)
    with open(name+'.jpg','wb') as f:
        f.write(img_res.content)
        f.close()

def main():
    name = input("请输入您的名字(最好不超过四个汉字)：")
    create_sign(name)
    print("您的签名已完成，以图片的形式保存在当前目录！")

if __name__ == "__main__":
    main()
