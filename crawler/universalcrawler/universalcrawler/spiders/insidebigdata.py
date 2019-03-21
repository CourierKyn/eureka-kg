# -*- coding: utf-8 -*-
import scrapy


class InsidebigdataSpider(scrapy.Spider):
    name = 'insidebigdata'
    allowed_domains = ['insidebigdata.com']
    start_urls = ['http://insidebigdata.com/']

    def parse(self, response):
        pass
