# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


# class XywyCrawlSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
#

# class DownMiddleware1(object):
#
#     def process_request(self, request, spider):
#         """
#         请求需要被下载时，经过所有下载器中间件的process_request调用
#         :param request:
#         :param spider:
#         :return:
#             None,继续后续中间件去下载；
#             Response对象，停止process_request的执行，开始执行process_response
#             Request对象，停止中间件的执行，将Request重新调度器
#             raise IgnoreRequest异常，停止process_request的执行，开始执行process_exception
#         """
#         print(request.url)
#         # print(123)
#         # request.method = 'POST'
#         return None
#
#     def process_response(self, request, response, spider):
#         """
#         spider处理完成，返回时调用
#         :param response:
#         :param result:
#         :param spider:
#         :return:
#             Response 对象：转交给其他中间件process_response
#             Request 对象：停止中间件，request会被重新调度下载
#             raise IgnoreRequest 异常：调用Request.errback
#         """
#         # print('response1')
#         return response
#
#     def process_exception(self, request, exception, spider):
#         """
#         当下载处理器(download handler)或 process_request() (下载中间件)抛出异常
#         :param response:
#         :param exception:
#         :param spider:
#         :return:
#             None：继续交给后续中间件处理异常；
#             Response对象：停止后续process_exception方法
#             Request对象：停止中间件，request将会被重新调用下载
#         """
#         print(122)
#         return None
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         # print(222)
#         # crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s

from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
import base64
import six
import random


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
            {'ip_port': '14.115.107.72:9797', 'user_pass': ''},
            # {'ip_port': '120.198.243.22:80', 'user_pass': ''},
            # {'ip_port': '111.8.60.9:8123', 'user_pass': ''},
            # {'ip_port': '101.71.27.120:80', 'user_pass': ''},
            # {'ip_port': '122.96.59.104:80', 'user_pass': ''},
            # {'ip_port': '122.224.249.122:8088', 'user_pass': ''},
        ]
        proxy = random.choice(PROXIES)
        print(proxy)
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = to_bytes("http://%s" % proxy['ip_port'])
            # encoded_user_pass = base64.encodestring(to_bytes(proxy['user_pass']))
            encoded_user_pass = base64.encodebytes(to_bytes(proxy['user_pass']))
            request.headers['Proxy-Authorization'] = to_bytes('Basic ' + encoded_user_pass)
            print("**************ProxyMiddleware have pass************" + proxy['ip_port'])
        else:
            print("**************ProxyMiddleware no pass************" + proxy['ip_port'])
            request.meta['proxy'] = to_bytes("http://%s" % proxy['ip_port'])