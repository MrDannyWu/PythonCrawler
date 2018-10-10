import requests
from bs4 import BeautifulSoup

def create_sign(name):
    url = 'http://www.jiqie.com/a/re19.php'
    form_data = {
        'id': name,
        'idi': 'jiqie',
        'id1': '1002',
        'id2': '20',
        'id3':'#000000',
        'id4':'#000000',
        'id5':'2',
        'id6':'',
        }
    web_data = requests.post(url,data=form_data)
    web_data.encoding = 'utf-8'
    soup = BeautifulSoup(web_data.text,'lxml')
    #print(soup)

    tu = "http://www.jiqie.com" + soup.select('img')[0].get('src').split('.')[2] + "." + soup.select('img')[0].get('src').split('.')[3]
    #print(tu)
    img_res = requests.get(tu)
    with open(name+'.jpg','wb') as f:
        f.write(img_res.content)
create_sign("DannyWu")
def main():
    name = input("请输入您的名字：")
    create_sign(name)
    print("您的签名已完成，以图片的形式保存在当前目录！")

if __name__ == "__main__":
    main()
