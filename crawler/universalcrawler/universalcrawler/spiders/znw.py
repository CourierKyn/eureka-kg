# -*- coding: utf-8 -*-
import scrapy


class ComSpider(scrapy.Spider):
    name = 'znw'
    allowed_domains = ['znw.com.cn']
    start_urls = ['http://znw.com.cn/']

    def parse(self, response):
        pass
