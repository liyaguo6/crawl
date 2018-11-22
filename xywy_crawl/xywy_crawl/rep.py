
"""
自定义去重规则：
步骤一：写一个去重规则的类
步骤二：在settings文件中注册DUPEFILTER_CLASS = 'xywy_crawl.rep.RepeatUrl'  #自定义去重规则
步骤三：在将url加入调度器之前，定义：dont_filter = False
"""

class RepeatUrl:
    def __init__(self):
        self.visited_url = set() # 放在当前服务的内存

    @classmethod
    def from_settings(cls, settings):
        """
        初始化时，调用
        :param settings:
        :return:
        """
        return cls()

    def request_seen(self, request):
        """
        检测当前请求是否已经被访问过
        :param request:
        :return: True表示已经访问过；False表示未访问过
        """
        if request.url in self.visited_url:
            return True
        self.visited_url.add(request.url)
        return False

    def open(self):
        """
        开始爬去请求时，调用
        :return:
        """
        print('open 去重')

    def close(self, reason):
        """
        结束爬虫爬取时，调用
        :param reason:
        :return:
        """
        # print(self.visited_url)
        print('close 去重')

    def log(self, request, spider):
#         """
#         记录日志
#         :param request:
#         :param spider:
#         :return:
#         """
        print('repeat', request.url)