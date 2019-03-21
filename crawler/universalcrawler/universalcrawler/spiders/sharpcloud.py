# -*- coding: utf-8 -*-
import scrapy


class SharpcloudSpider(scrapy.Spider):
    name = 'sharpcloud'
    allowed_domains = ['sharpcloud.cn']
    start_urls = ['http://sharpcloud.cn/']

    def parse(self, response):
        pass
