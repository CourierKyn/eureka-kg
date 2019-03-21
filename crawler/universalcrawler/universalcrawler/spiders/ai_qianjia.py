# -*- coding: utf-8 -*-
import scrapy


class QianjiaSpider(scrapy.Spider):
    name = 'qianjia'
    allowed_domains = ['ai.qianjia.com']
    start_urls = ['http://ai.qianjia.com/']

    def parse(self, response):
        pass
