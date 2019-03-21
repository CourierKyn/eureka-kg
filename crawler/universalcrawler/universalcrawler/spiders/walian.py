# -*- coding: utf-8 -*-
import scrapy


class WalianSpider(scrapy.Spider):
    name = 'walian'
    allowed_domains = ['walian.cn']
    start_urls = ['http://walian.cn/']

    def parse(self, response):
        pass
