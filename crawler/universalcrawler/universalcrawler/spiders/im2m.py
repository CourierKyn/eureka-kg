# -*- coding: utf-8 -*-
import scrapy


class Im2mComSpider(scrapy.Spider):
    name = 'im2m.com'
    allowed_domains = ['im2m.com.cn']
    start_urls = ['http://im2m.com.cn/']

    def parse(self, response):
        pass
