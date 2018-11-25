# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class XywyCrawlSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        # crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self,response, spider):
        """
        下载完成，执行，让后交给parse处理
        :param spider:
        :return:
        """
        print(response.url)
        # Called for each response that goes through the spider
        # middleware and into the spider.
        print(8)
        # Should return None or raise an exception.
        return None

    def process_spider_output(self,response, result, spider):
        """
        spider处理完成，返回时调用
        :param result:
        :param spider:
        :return: 必须返回包含 Request 或 Item 对象的可迭代对象(iterable)

        """
        # Called with the results returned from the Spider, after
        # it has processed the response.
        print(10)
        print(list(result))
        # Must return an iterable of Request, dict or Item objects.
        # for i in result:
        #     yield i
        return result

    def process_spider_exception(self,response, exception, spider):
        """
        异常处理
        :param response:
        :param exception:
        :param spider:
        :return:None  None,继续交给后续中间件处理异常；含 Response 或 Item 的可迭代对象(iterable)，交给调度器或pipeline
        """
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.
        print(11)
        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self,start_requests, spider):
        """
        起始url
        :param start_requests:
        :param spider:
        :return:
        """
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        # print(12)
        # for r in start_requests:
        #     # print(r)
        #     yield r
        # print(start_requests)
        return start_requests


    # def spider_opened(self, spider):
    #     spider.logger.info('Spider opened: %s' % spider.name)


class DownMiddleware1(object):

    def process_request(self, request, spider):
        """
        请求需要被下载时，经过所有下载器中间件的process_request调用
        :param request:
        :param spider:
        :return:
            None,继续后续中间件去下载；
            Response对象，停止process_request的执行，开始执行process_response
            Request对象，停止中间件的执行，将Request重新调度器
            raise IgnoreRequest异常，停止process_request的执行，开始执行process_exception
        """
        print(request.url)
        # print(123)
        # request.method = 'POST'
        return None

    def process_response(self, request, response, spider):
        """
        spider处理完成，返回时调用
        :param response:
        :param result:
        :param spider:
        :return:
            Response 对象：转交给其他中间件process_response
            Request 对象：停止中间件，request会被重新调度下载
            raise IgnoreRequest 异常：调用Request.errback
        """
        return response

    def process_exception(self, request, exception, spider):
        """
        当下载处理器(download handler)或 process_request() (下载中间件)抛出异常
        :param response:
        :param exception:
        :param spider:
        :return:
            None：继续交给后续中间件处理异常；
            Response对象：停止后续process_exception方法
            Request对象：停止中间件，request将会被重新调用下载
        """
        print(122)
        return None

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        # print(222)
        # crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

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
            # {'ip_port': '14.115.107.72:9797', 'user_pass': ''},
            {'ip_port': '101.236.57.99:8866', 'user_pass': None},
            {'ip_port': '61.135.217.7:80', 'user_pass':None},
            {'ip_port': '111.8.60.9:8123', 'user_pass': None},
            {'ip_port': '180.118.243.169:53128', 'user_pass': None},
            {'ip_port': '114.230.218.175:8010', 'user_pass': None},
            {'ip_port': '58.52.171.159:808', 'user_pass':None},
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
        print(request.url)
        return None

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        print(222)
        # crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s