# -*- coding: utf-8 -*-
import scrapy


class IotcnOrgSpider(scrapy.Spider):
    name = 'iotcn'
    allowed_domains = ['iotcn.org.cn']
    start_urls = ['http://iotcn.org.cn/']

    def parse(self, response):
        pass
