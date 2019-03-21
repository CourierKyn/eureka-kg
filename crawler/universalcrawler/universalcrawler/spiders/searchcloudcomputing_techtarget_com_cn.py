# -*- coding: utf-8 -*-
import scrapy


class SearchcloudcomputingTechtargetSpider(scrapy.Spider):
    name = 'searchcloudcomputing.techtarget.com.cn'
    allowed_domains = ['searchcloudcomputing.techtarget.com.cn']
    start_urls = ['http://searchcloudcomputing.techtarget.com.cn/']

    def parse(self, response):
        pass
