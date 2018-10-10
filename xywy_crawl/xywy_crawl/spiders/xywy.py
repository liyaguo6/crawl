# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector,Selector
from scrapy.http.cookies import CookieJar


class XywySpider(scrapy.Spider):
    name = "xywy"
    allowed_domains = ["club.xywy.com"]
    start_urls = ['http://club.xywy.com/list_answer.htm']
    page_url_list =[]


    def start_requests(self):
        for url in self.start_urls:
            print(url)
            yield Request(url=url,dont_filter=True,callback=self.parse1)

    def parse1(self, response):
        # print(response.text)
        hxs = Selector(response=response)

        # cookie_jar = CookieJar()
        # cookie_jar.extract_cookies(response, response.request)
        url_list=hxs.xpath('//table[@class="f12 kstable"]//a[@class="btn-a hov_clor"]/@href').extract()
        for url in url_list:
            yield Request(
                url = url,
                method='GET',
                # cookies=cookie_jar,
                callback=self.parse2,
                dont_filter=True,
            )
        url_page = hxs.xpath('//div[@class="bore4 pt10"]//a[@target="_self"]/@href').extract()
        for url in url_page:
            if url not in self.page_url_list:
                self.page_url_list.append(url)
                yield Request(url="http://club.xywy.com%s"%(url), dont_filter=True, callback=self.parse1)

    def parse2(self, response):
        hxs = Selector(response=response)
        answer = hxs.xpath('//div[@class="clearfix pl29 pr15"]//p[@class="fl dib fb"]/text()').extract_first()
        print(answer)
