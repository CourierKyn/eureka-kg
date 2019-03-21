# -*- coding: utf-8 -*-
import scrapy


class AtyunSpider(scrapy.Spider):
    name = 'atyun'
    allowed_domains = ['atyun.com']
    start_urls = ['http://atyun.com/']

    def parse(self, response):
        pass
