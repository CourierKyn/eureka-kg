# -*- coding: utf-8 -*-
import scrapy
import json
import re


class WikidataSpider(scrapy.Spider):
    name = 'wikidata'
    allowed_domains = ['wikidata.org']

    def start_requests(self):
        base_url = 'https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&language=en&uselang=en&typ' \
                   'e=item&search='
        for line in open('E.txt'):
            entity = line[:-1].replace(',', '')
            if '(' in entity:
                yield scrapy.Request(base_url + ' '.join(re.split(r' *\(.+?\) *', entity)).rstrip(),
                                     meta={'entity': entity})
                yield scrapy.Request(base_url + re.findall(r'\((.+?)\)', entity)[0],
                                     meta={'entity': entity, 'mark': True})
            elif ' / ' in entity:
                for i in entity.split(' / '):
                    yield scrapy.Request(base_url + i, meta={'entity': entity})
            else:
                yield scrapy.Request(base_url + entity, meta={'entity': entity})

    def parse(self, response):
        if response.meta.get('mark'):
            yield {'entity': response.meta['entity'], 'mark': True, 'response': json.loads(response.text)}
        else:
            yield {'entity': response.meta['entity'], 'response': json.loads(response.text)}
