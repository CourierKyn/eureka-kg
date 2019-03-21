# -*- coding: utf-8 -*-
import scrapy


class JournalofcloudcomputingSpringeropenSpider(scrapy.Spider):
    name = 'journalofcloudcomputing.springeropen'
    allowed_domains = ['journalofcloudcomputing.springeropen.com']
    start_urls = ['http://journalofcloudcomputing.springeropen.com/']

    def parse(self, response):
        pass
