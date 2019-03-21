# -*- coding: utf-8 -*-
import scrapy


class WlitSpider(scrapy.Spider):
    name = 'wlit'
    allowed_domains = ['wlit.cn']
    start_urls = ['http://wlit.cn/']

    def parse(self, response):
        pass
