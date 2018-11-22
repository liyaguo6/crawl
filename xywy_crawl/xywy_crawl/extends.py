
"""
自定义信号 自定义扩展时，利用信号在指定位置注册制定操作
步骤一：写一个信号扩展的类，在from_crawler 中注册在哪里使用信号
步骤二：在settings注册信号的启动文件
EXTENSIONS = {
   'xywy_crawl.extends.MyExtension': 300,
}
"""

from scrapy import signals


class MyExtension(object):
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_crawler(cls, crawler):
        val = crawler.settings.get('VAR')
        ext = cls(val)

        # 在scrapy中注册信号： spider_opened，触发信号时执行的函数
        crawler.signals.connect(ext.opened, signal=signals.spider_opened)
        # 在scrapy中注册信号： spider_closed，
        crawler.signals.connect(ext.closed, signal=signals.spider_closed)

        return ext

    def opened(self, spider):
        # print(spider.name)
        print('open 信号')

    def closed(self, spider):
        # print(spider.name)
        # print(self.value)
        print('close 信号')