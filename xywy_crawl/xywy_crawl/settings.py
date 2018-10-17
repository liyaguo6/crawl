# -*- coding: utf-8 -*-

# Scrapy settings for xywy_crawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

# 1. 爬虫名称
BOT_NAME = 'xywy_crawl'
# 2. 爬虫应用路径
SPIDER_MODULES = ['xywy_crawl.spiders']
NEWSPIDER_MODULE = 'xywy_crawl.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 3. 客户端 user-agent请求头
#USER_AGENT = 'xywy_crawl (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 5. 并发请求数
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 6. 延迟下载秒数
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#单域名访问并发数，并且延迟下次秒数也应用在每个域名
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 单IP访问并发数，如果有值则忽略：CONCURRENT_REQUESTS_PER_DOMAIN，并且延迟下次秒数也应用在每个IP
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 8. 是否支持cookie，cookiejar进行操作cookie
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# 9. Telnet用于查看当前爬虫的信息，操作爬虫等...
#    使用telnet ip port ，然后通过命令操作
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 10. 默认请求头
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
#11 爬虫中间件
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    # 'xywy_crawl.middlewares.XywyCrawlSpiderMiddleware': 543,
#    'xywy_crawl.middlewares.DownMiddleware1': 300,
# }

# Enable or disable downloader middlewares
#12下载中间件
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'xywy_crawl.middlewares.DownMiddleware1': 543,
# }


#13自定义扩展，基于信号进行调用
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'xywy_crawl.extensions.MyExtension': 300,
# }



# 13. 爬虫允许的最大深度，可以通过meta查看当前深度；0表示无深度
# DEPTH_LIMIT = 3

# 14. 爬取时，0表示深度优先Lifo(默认)；1表示广度优先FiFo

# 后进先出，深度优先
# DEPTH_PRIORITY = 0
# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleLifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.LifoMemoryQueue'
# 先进先出，广度优先

# DEPTH_PRIORITY = 1
# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

# 15. 调度器队列
# SCHEDULER = 'scrapy.core.scheduler.Scheduler'
# from scrapy.core.scheduler import Scheduler

# DUPEFILTER_CLASS = 'scrapy.dupefilters.RFPDupeFilter'

DUPEFILTER_CLASS = 'xywy_crawl.dupefilters.WwwDupeFilter'  #自定义去重规则








# Configure item pipelines  定义pipeline处理请求
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'xywy_crawl.pipelines.XywyCrawlPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# 17. 自动限速算法
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 18. 自定制命令
COMMANDS_MODULE ="xywy_crawl.commands"

"""
19. 代理，需要在环境变量中设置
    from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

    方式一：使用默认
        os.environ
        {
            http_proxy:http://root:woshiniba@192.168.11.11:9999/
            https_proxy:http://192.168.11.11:9999/
        }
    方式二：使用自定义下载中间件

    def to_bytes(text, encoding=None, errors='strict'):
        if isinstance(text, bytes):
            return text
        if not isinstance(text, six.string_types):
            raise TypeError('to_bytes must receive a unicode, str or bytes '
                            'object, got %s' % type(text).__name__)
        if encoding is None:
            encoding = 'utf-8'
        return text.encode(encoding, errors)

    class ProxyMiddleware(object):
        def process_request(self, request, spider):
            PROXIES = [
                {'ip_port': '111.11.228.75:80', 'user_pass': ''},
                {'ip_port': '120.198.243.22:80', 'user_pass': ''},
                {'ip_port': '111.8.60.9:8123', 'user_pass': ''},
                {'ip_port': '101.71.27.120:80', 'user_pass': ''},
                {'ip_port': '122.96.59.104:80', 'user_pass': ''},
                {'ip_port': '122.224.249.122:8088', 'user_pass': ''},
            ]
            proxy = random.choice(PROXIES)
            if proxy['user_pass'] is not None:
                request.meta['proxy'] = to_bytes（"http://%s" % proxy['ip_port']）
                encoded_user_pass = base64.encodestring(to_bytes(proxy['user_pass']))
                request.headers['Proxy-Authorization'] = to_bytes('Basic ' + encoded_user_pass)
                print "**************ProxyMiddleware have pass************" + proxy['ip_port']
            else:
                print "**************ProxyMiddleware no pass************" + proxy['ip_port']
                request.meta['proxy'] = to_bytes("http://%s" % proxy['ip_port'])

    DOWNLOADER_MIDDLEWARES = {
       'step8_king.middlewares.ProxyMiddleware': 500,
    }

"""

DOWNLOADER_MIDDLEWARES = {
   'xywy_crawl.middlewares.ProxyMiddleware': 500,
}