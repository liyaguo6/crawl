# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import csv
from scrapy.exceptions import DropItem

class XywyCrawlPipeline(object):
    def __init__(self):
        self.f = None

    def process_item(self, item, spider):
        """

        :param item: 爬虫中yield回来的对象
        :param spider:  爬虫对象
        :return:
        """
        if spider.name == "xywy":
            # print(item["answer"])
            # print(item["question"])
            # print(item["same_question"])
            # print(item["keywords"])
            # sample = list([item["keywords"][0],item["keywords"][1],item["question"],item["answer"]]).extend(item["same_question"])
            sample = [item["keywords"][0],item["keywords"][1],item["question"],item["answer"]]+item["same_question"]
            self.f.writerow(sample)
            # 将item传递给下一个pipeline的process_item方法
            # return item
        raise DropItem()  #截断传递数据

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        print("执行pipeline的from_crawler,进行实例化对象")
        # val = crawler.settings.get('MMMM')
        return cls()

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print('打开爬虫')
        self.f = csv.writer(open("test.csv",'a+',encoding="gbk",newline=''),dialect="excel")



    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        print('关闭爬虫')
        self.f.close()