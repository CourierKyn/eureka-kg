# -*- coding: utf-8 -*-
import scrapy


class BlockchaintrainingallianceSpider(scrapy.Spider):
    name = 'blockchaintrainingalliance'
    allowed_domains = ['blockchaintrainingalliance.com']
    start_urls = ['http://blockchaintrainingalliance.com/']

    def parse(self, response):
        pass
