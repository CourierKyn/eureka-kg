# -*- coding: utf-8 -*-
import scrapy


class QukuaiwangSpider(scrapy.Spider):
    name = 'qukuaiwang'
    allowed_domains = ['qukuaiwang.com.cn']
    start_urls = ['http://qukuaiwang.com.cn/']

    def parse(self, response):
        pass
