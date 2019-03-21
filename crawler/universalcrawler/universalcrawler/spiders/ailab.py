# -*- coding: utf-8 -*-
import scrapy


class AilabSpider(scrapy.Spider):
    name = 'ailab'
    allowed_domains = ['ailab.cn']
    start_urls = ['http://ailab.cn/']

    def parse(self, response):
        pass
