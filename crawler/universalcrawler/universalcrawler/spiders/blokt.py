# -*- coding: utf-8 -*-
import scrapy


class BloktSpider(scrapy.Spider):
    name = 'blokt'
    allowed_domains = ['blokt.com']
    start_urls = ['http://blokt.com/']

    def parse(self, response):
        pass
