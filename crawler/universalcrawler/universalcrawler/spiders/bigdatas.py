# -*- coding: utf-8 -*-
import scrapy


class BigdatasSpider(scrapy.Spider):
    name = 'bigdatas'
    allowed_domains = ['bigdatas.cn']
    start_urls = ['http://bigdatas.cn/']

    def parse(self, response):
        pass
