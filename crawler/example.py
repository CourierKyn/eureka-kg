import requests
from bs4 import BeautifulSoup
import pprint
import re
import json


def get(url):
    try:
        return requests.get(url)
    except Exception as e:
        print(e, 'from', url)


def parse(r, url_prefix):
    if r is None:
        return
    soup = BeautifulSoup(r.text, 'lxml')
    for sub_soup in soup.select('body div.quote'):
        text = next((i.string[1:-1] for i in sub_soup.select('span.text')), None)
        author = next((i.string for i in sub_soup.select('span .author')), None)
        author_url = next((url_prefix + i['href'] for i in sub_soup.select('span .author ~ a')), None)
        tags = [(i.string, url_prefix + i['href']) for i in sub_soup.select('div.tags > a.tag')]
        yield {
            'text': text,
            'author': author,
            'author_url': author_url,
            'tags': tags,
        }
    for next_page in soup.select('li.next > a'):
        for i in parse(get(url_prefix + next_page['href']), url_prefix):
            yield i


if __name__ == '__main__':
    start_url = 'http://quotes.toscrape.com/'
    url_prefix = re.findall(r'^((https?:)?(//)?.+?)(?=/|$)', start_url)[0][0]
    out = list(parse(get(start_url), url_prefix))
    pprint.pprint(out)
    with open('out.json', 'w') as f:
        json.dump(out, f, indent=4)
