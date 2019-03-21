# -*- coding: utf-8 -*-
import scrapy


class CloudaveSpider(scrapy.Spider):
    name = 'cloudave'
    allowed_domains = ['cloudave.com']
    start_urls = ['http://cloudave.com/']

    def parse(self, response):
        pass
