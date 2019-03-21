# -*- coding: utf-8 -*-
import scrapy


class A52aiSpider(scrapy.Spider):
    name = '52ai'
    allowed_domains = ['52ai.com']
    start_urls = ['http://52ai.com/']

    def parse(self, response):
        pass
