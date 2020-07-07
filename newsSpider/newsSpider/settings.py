# -*- coding: utf-8 -*-

BOT_NAME = 'newsSpider'

SPIDER_MODULES = ['newsSpider.spiders']
NEWSPIDER_MODULE = 'newsSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'cookie': 'SINAGLOBAL=172.16.7.128_1539008461.893003; SCF=AiaI033UaxxhVHsojag4PglU4mNJlL_ovhETL-lbZk2LI-MMqnSCu3K1VEqpsqAkMN7dXgjpEJAyLVDkGTAMc5o.; sso_info=v02m6alo5qztKWRk5ilkKOUpY6DhKWRk5iljpOgpY6UmKWRk4yljoOApY6DiKWRk4yljoOApY6DiKWRk4yljoOApY6DiKWRk5iljpOcpZCjmKWRk5SljoOUpY6DpKadlqWkj5OIs46TkLGMo6CyjaOMwA==; U_TRS1=0000005d.128d493c.5bdd9334.0d2d437a; UOR=,news.sina.com.cn,; Apache=36.34.4.207_1542285896.26731; lxlrttp=1541383354; ULV=1542286572263:2:2:2:36.34.4.207_1542285896.26731:1542285897096; SUB=_2A2526Ry9DeRhGeRN4lYQ8ibOzT-IHXVVnwl1rDV_PUNbm9AKLVP7kW9NU2MA0lk87UlvZNPFlC23NQeecWWy1Ur_; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWjEvCkWWL6qdHWgHsA.1zq5NHD95QEe0.XeKzReoq0Ws4DqcjiKPi2qg4VwHUf; ALF=1573822573; U_TRS2=000000cf.f55b9f8.5bed6cee.77665a37; UM_distinctid=1671771dce68-0645e9cfa907a9-4313362-100200-1671771dce81a5; CNZZDATA1261221115=254302524-1542283470-https%253A%252F%252Fnews.sina.com.cn%252F%7C1542283470; CNZZDATA5581086=cnzz_eid%3D99080340-1542285299-https%253A%252F%252Fnews.sina.com.cn%252F%26ntime%3D1542285299; CNZZDATA5399792=cnzz_eid%3D1467705105-1542282565-https%253A%252F%252Fnews.sina.com.cn%252F%26ntime%3D1542282565; CNZZDATA5661630=cnzz_eid%3D568443282-1542283299-https%253A%252F%252Fnews.sina.com.cn%252F%26ntime%3D1542283299',
   'referer': 'https://news.sina.com.cn/china/',
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'newsSpider.middlewares.NewsspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'newsSpider.middlewares.NewsspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'newsSpider.pipelines.NewsspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
