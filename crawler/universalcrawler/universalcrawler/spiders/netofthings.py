# -*- coding: utf-8 -*-
import scrapy


class NetofthingsSpider(scrapy.Spider):
    name = 'netofthings'
    allowed_domains = ['netofthings.cn']
    start_urls = ['http://netofthings.cn/']

    def parse(self, response):
        pass
