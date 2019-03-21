# -*- coding: utf-8 -*-
import scrapy


class A100qklSpider(scrapy.Spider):
    name = '100qkl'
    allowed_domains = ['100qkl.com']
    start_urls = ['http://100qkl.com/']

    def parse(self, response):
        pass
