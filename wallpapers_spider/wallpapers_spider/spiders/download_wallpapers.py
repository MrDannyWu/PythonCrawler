import scrapy
from wallpapers_spider.items import WallpapersSpiderItem
import requests


class DownloadWallpapersSpider(scrapy.Spider):
    name = 'download_wallpapers'
    allowed_domains = ['wallpaperhunt.net']
    start_urls = ['http://wallpaperhunt.net/?page={}'.format(i + 1) for i in range(73)]
    headers = {
        'cookie': '__cfduid=de1874a503e2cd3af91b16e8fb6097a181604823296; _ga=GA1.2.1147081149.1604823297; _gid=GA1.2.1885287730.1604823297; __gads=ID=1567bda77160b40c-22417a7aa2c4009f:T=1604823297:RT=1604823297:S=ALNI_MZGNTqBdYpKSK21HSSFBiHTx1lB0w; _gat=1; XSRF-TOKEN=eyJpdiI6InA4TXJnXC9YVXpTTjQyZXdVXC9RNGJJdz09IiwidmFsdWUiOiJTUXp6UUhzaXhcL1hrZFB5cGtXTmJldm13WWVPcGVWUmhZY0JGRDd5TDVMUmppUzBoMUlGVnRjWjBuMFBBTURPT0ZpdTBkXC9UMG85amVIVVQ2SnhQYVhRPT0iLCJtYWMiOiI4MzBiYTQ1YzEyNTExYzIwZTdhMDE2MmRjYWY5ZjI2NjA2MjA1ZGYzNzMxZTBkMDM2ODQ0ZWUwZjVmNmQ4M2YwIn0%3D; laravel_session=eyJpdiI6InpLVWVLNW10K3k0M1gwNUN5MkFrVUE9PSIsInZhbHVlIjoiQ1VvR3N6RVJmVWtROEUxblFEem1xM1lVWHZyT1pNQWNUWFQzUTlKNUMxQU53YjBucDlpZW9PdEJnaTNhSFZ5REdTTG9INHBKK3h1NnZZNnVtOWRqYUE9PSIsIm1hYyI6IjEyMDZiOGUzYTA0NWUyMzFhYTNiOTViZmM2OWYzNmZiNTQzMGE2NTVmMWZlZjEyMDFkZDQxYTNiM2I1MjIyYjgifQ%3D%3D',
        'referer': 'https://wallpaperhunt.net/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    def parse(self, response):
        # print(response.status)
        # print(response.text)
        a_list = response.xpath('//a[@class="wallpaper-preview-collection-link"]/@href').extract()
        for i in a_list:
            # print(i)
            yield scrapy.Request(url=i, callback=self.parse_pic_url)

    def parse_pic_url(self, response):
        item = WallpapersSpiderItem()
        a_list = response.xpath('//a[@class="wallpaper-dl"]/@href').extract()
        url_list = []
        for j in a_list:
            pic_name = 'pics/' + j.split('f=')[-1].strip()
            resp = requests.get(url=j, headers=self.headers)
            with open(pic_name, 'wb') as f:
                f.write(resp.content)
                f.close()

        # item['pic_url'] = url_list
        # yield item

            # print(j)
            # yield scrapy.Request(url=j, callback=self.parse_download_pic)
    # def parse_download_pic(self, response):
    #     print('###############', response.request.url)
    #     pic_name = 'pics/' + response.request.url.split('f=')[-1]
    #     with open(pic_name, 'wb') as f:
    #         f.write(response.content)
    #         f.close

