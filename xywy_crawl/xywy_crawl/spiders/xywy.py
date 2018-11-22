# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector,Selector
from scrapy.http.cookies import CookieJar
from bs4 import BeautifulSoup
from ..items import XywyCrawlItem
from scrapy.dupefilters import RFPDupeFilter

class XywySpider(scrapy.Spider):
    name = "xywy"
    allowed_domains = ["club.xywy.com"]
    start_urls = ['http://club.xywy.com/list_answer.htm']
    page_url_list =[]


    def start_requests(self):
        for url in self.start_urls:
            # print(url)
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
                dont_filter=False,
            )
        # url_page = hxs.xpath('//div[@class="bore4 pt10"]//a[@target="_self"]/@href').extract()
        # for url in url_page:
        #     if url not in self.page_url_list:
        #         self.page_url_list.append(url)
        #         yield Request(url="http://club.xywy.com%s"%(url), dont_filter=True, callback=self.parse1)

    def parse2(self, response):
        hxs = Selector(response=response)
        first_question = hxs.xpath('//div[@class="clearfix pl29 pr15"]//p[@class="fl dib fb"]/text()').extract_first()
        answer_list= hxs.xpath('//div[@class="pt15 f14 graydeep  pl20 pr20 deepblue"]').extract()
        question_list = hxs.xpath('//div[@class="relate-ques"]/span/text()').extract()
        answer = ",".join(answer_list)
        soup = BeautifulSoup(answer, features="lxml")
        answer_text = soup.find('div').get_text()
        keywords= hxs.xpath('//div[@class="w980 clearfix bc f12 btn-a pr"]/p[@class="pt10 pb10 lh180 znblue normal-a"]/a/text()').extract()[-2:]
        print(keywords)
        # yield XywyCrawlItem(answer=answer_text,question=first_question,same_question=question_list,keywords=keywords)
