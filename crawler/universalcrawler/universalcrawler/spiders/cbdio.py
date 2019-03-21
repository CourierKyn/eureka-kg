# -*- coding: utf-8 -*-
import scrapy


class CbdioSpider(scrapy.Spider):
    name = 'cbdio'
    allowed_domains = ['cbdio.com']
    start_urls = ['http://cbdio.com/']

    def parse(self, response):
        pass
