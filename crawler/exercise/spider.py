import requests
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
import re
from hashlib import md5
import os
from multiprocessing import Pool
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6'}


def get_page_index(offset, keyword):
    url = 'https://www.toutiao.com/search_content/'
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3
    }
    try:
        response = requests.get(url, params=data, headers=headers)
        if response.status_code == 200:
            return response.text
        print(response.status_code, 'from index page')
        return None
    except RequestException:
        print('RequestException from index page')
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data['data']:
            yield item.get('article_url')


def get_page_detail(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        print(response.status_code, 'from detail page')
        return None
    except RequestException:
        print('RequestException from detail page')
        return None


def parse_page_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    if soup.select('title'):
        title = soup.select('title')[0].get_text()
    else:
        title = None
    image_pattern = re.compile(r'gallery: JSON.parse\("(.+)"\),')
    result = image_pattern.search(html)
    if result:
        data = json.loads(result.group(1).replace('\\', ''))
        if data and 'sub_images' in data.keys():
            sub_images = data['sub_images']
            images = [sub_image.get('url') for sub_image in sub_images]
            return {
                'title': title,
                'images': images
            }


def download_image(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
        print(response.status_code, 'from image')
        return None
    except RequestException:
        print('RequestException from image')
        return None


def save_image(content):
    path = md5(content).hexdigest() + '.' + 'jpg'
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(content)


def main(d):
    html = get_page_index(d['offset'], d['keyword'])
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html)
            if result:
                print('downloading images from', result['title'])
                for image_url in result['images']:
                    content = download_image(image_url)
                    if content:
                        save_image(content)


if __name__ == '__main__':
    pool = Pool()
    keyword = input('抓取图片的关键词（比如萌妹）：')
    if not keyword:
        keyword = '萌妹'
    groups = [{'offset': i, 'keyword': keyword} for i in range(0, 300, 20)]
    pool.map(main, groups)
