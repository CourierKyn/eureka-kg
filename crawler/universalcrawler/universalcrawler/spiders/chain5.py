# -*- coding: utf-8 -*-
import scrapy


class Chain5Spider(scrapy.Spider):
    name = 'chain5'
    allowed_domains = ['chain5.cc']
    start_urls = ['http://chain5.cc/']

    def parse(self, response):
        pass
