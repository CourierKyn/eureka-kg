# -*- coding: utf-8 -*-
import scrapy


class AitrendsSpider(scrapy.Spider):
    name = 'aitrends'
    allowed_domains = ['aitrends.com']
    start_urls = ['http://aitrends.com/']

    def parse(self, response):
        pass
