# -*- coding: utf-8 -*-
import scrapy


class CnelcSpider(scrapy.Spider):
    name = 'yjs.cnelc'
    allowed_domains = ['yjs.cnelc.com']
    start_urls = ['http://yjs.cnelc.com/']

    def parse(self, response):
        pass
