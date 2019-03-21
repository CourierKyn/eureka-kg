# -*- coding: utf-8 -*-
import scrapy


class QkzjSpider(scrapy.Spider):
    name = 'qkzj'
    allowed_domains = ['qkzj.com']
    start_urls = ['http://qkzj.com/']

    def parse(self, response):
        pass
