# -*- coding: utf-8 -*-
import scrapy
from readability import Document


class HibtcSpider(scrapy.Spider):
    name = 'hibtc'
    allowed_domains = ['hibtc.org']
    start_urls = ['http://hibtc.org/']
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                             'Version/12.0.3 Safari/605.1.15'}

    def parse(self, response):
        doc = Document(response.text)
        yield {
            'url': response.url,
            'short_title': doc.short_title(),
            'summary': doc.summary(html_partial=True),
        }
        for next_page in response.css('a::attr("href")'):
            yield response.follow(next_page, self.parse)
