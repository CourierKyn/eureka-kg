# -*- coding: utf-8 -*-
import scrapy


class A50cnnetSpider(scrapy.Spider):
    name = '50cnnet'
    allowed_domains = ['50cnnet.com']
    start_urls = ['http://50cnnet.com/']

    def parse(self, response):
        pass
