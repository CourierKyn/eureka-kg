# -*- coding: utf-8 -*-
import scrapy


class IotwormSpider(scrapy.Spider):
    name = 'iotworm'
    allowed_domains = ['iotworm.com']
    start_urls = ['http://iotworm.com/']

    def parse(self, response):
        pass
