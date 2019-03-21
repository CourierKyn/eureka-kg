# -*- coding: utf-8 -*-
import scrapy


class CoindeskSpider(scrapy.Spider):
    name = 'coindesk'
    allowed_domains = ['coindesk.com']
    start_urls = ['http://coindesk.com/']

    def parse(self, response):
        pass
