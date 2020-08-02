"""
auth: DannyWu
site: http://www.idannywu.com
"""
import requests
from lxml import etree
from fontTools.ttLib import TTFont
from bs4 import BeautifulSoup


# 下载字体文件
def download_font_file(font_file_url, save_font_file):
    res = requests.get(font_file_url)
    with open(save_font_file, 'wb')as w:
        w.write(res.content)
        w.close()


def read_file_to_list(file_name):
    with open(file_name, 'r')as read:
        result = read.readlines()
        read.close()
    return result


def num_font_reflect_to_csv(font_file, save_font_xml_file, save_font_csv_file):
    with open(save_font_csv_file, 'w') as f:
        f.close()
    TTFont(font_file).saveXML(save_font_xml_file)
    with open(save_font_xml_file, 'r', encoding='utf-8')as rea:
        font_str = rea.read()
        # print(font_str)
        rea.close()
    soup_1 = BeautifulSoup(font_str, 'lxml')
    ttglyphs = soup_1.select('ttglyph')
    for each in ttglyphs:
        # print(each)
        name = each.get('name')
        if name != 'x' and name != 'glyph00000':
            name = each.get('name')
            xmin = str(each.get('xmin'))
            ymin = str(each.get('ymin'))
            xmax = str(each.get('xmax'))
            ymax = str(each.get('ymax'))
            print(name, xmin + ymin + xmax + ymax)
            with open(save_font_csv_file, 'a') as f:
                f.write('0,' + name + ',' + xmin + ymin + xmax + ymax + '\n')
                f.close()


def get_html(web_url, web_header):
    try:
        resp = requests.get(web_url, headers=web_header)
        return resp.text
    except:
        print('Connection error...')


if __name__ == '__main__':
    url = 'https://maoyan.com/'
    header = {
        'Connection': 'keep-alive',
        'Cookie': '_lxsdk_cuid=16b5bd06184c8-0b2dca8b9c8633-37c153e-1fa400-16b5bd06184c8; uuid_n_v=v1; uuid=92A8C5A08F8411E99F6803B81A8BA4474E846E27C7074534A9ED5DEB1BA39883; _csrf=9598285dad28c4897795f58790e87abe402b749974563042cb9f7512942ec4c2; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk=92A8C5A08F8411E99F6803B81A8BA4474E846E27C7074534A9ED5DEB1BA39883; __mta=149141385.1560613517801.1560613583753.1560613609005.5; _lxsdk_s=16b5bd06185-8a7-57d-d2e%7C%7C28',
        'Host': 'maoyan.com',
        'Referer': 'https://maoyan.com/films',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    }

    web_data = get_html(url, header)
    html = etree.HTML(web_data)
    soup = BeautifulSoup(web_data, 'lxml')
    print(soup.select('.stonefont'))
    print([x.text for x in soup.select('.stonefont')])
    styles = html.xpath('//style/text()')
    for style in styles:
        if '.woff' in str(style):
            font_url = 'http://' + str(style).split('.woff')[0].split("url('//")[-1] + '.woff'
    print(font_url)
    download_font_file(font_url, 'font.woff')
    num_font_reflect_to_csv('font.woff', 'font.xml', 'current_font.csv')
    # TTFont('E:\\Desktop\\20f48fd4e7156490dab8e18bfefcd8762080.woff').saveXML('E:\\Desktop\\font_1.xml')
    results_1 = read_file_to_list('example_font.csv')
    results_2 = read_file_to_list('current_font.csv')
    print(results_1)
    print(results_2)
    font_list = []
    for i in results_1:
        font_info_1 = i.strip().split(',')
        for j in results_2:
            font_info_2 = j.strip().split(',')
            if font_info_1[2] == font_info_2[2]:
                font_info_2[0] = font_info_1[0]
                print(font_info_1, '  ', font_info_2)
                font_list.append(font_info_2)
    print(font_list)

    ranking_num = html.xpath('//div[@class="ranking-box-wrapper"]/div/div/ul/li/a/span/span[@class="ranking-num-info"]/span[@class="stonefont"]/text()')
    ranking_name = html.xpath('//div[@class="ranking-box-wrapper"]/div/div/ul/li/a/span/span[@class="ranking-movie-name"]/text()')
    for i, j in zip(ranking_num, ranking_name):
        page_font_text = orig_data = i.encode('unicode-escape').decode('utf-8').replace('\\u', 'uni').upper().replace('UNI', 'uni')
        for k in font_list:
            if str(k[1]) in str(page_font_text):
                page_font_text = page_font_text.replace(str(k[1]), str(k[0]))
        print(j, ': ', page_font_text)

