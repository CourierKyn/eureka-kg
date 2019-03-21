# -*- coding: utf-8 -*-
import scrapy


class IothomeSpider(scrapy.Spider):
    name = 'iothome'
    allowed_domains = ['iothome.com']
    start_urls = ['http://iothome.com/']

    def parse(self, response):
        pass
