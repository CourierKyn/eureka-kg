# -*- coding: utf-8 -*-
import scrapy


class BlogBoschSiSpider(scrapy.Spider):
    name = 'blog.bosch-si'
    allowed_domains = ['blog.bosch-si.com']
    start_urls = ['http://blog.bosch-si.com/']

    def parse(self, response):
        pass
