import pandas as pd
import requests
from bs4 import BeautifulSoup
import json


def get(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        return requests.get(url, headers=headers)
    except Exception as e:
        print(e, 'from', url)


def parse(r):
    if r is None:
        return
    soup = BeautifulSoup(r.text, 'lxml')
    s = ''
    for content in soup.select("[class~=mw-parser-output]"):
        [c.extract() for c in content.p('sup')]
        s += content.p.get_text()
    return s


URL = "https://en.wikipedia.org/wiki/Ant_Financial"
data = {
    'url': URL,
    'name': URL.split('/')[-1],
    'description': parse(get(URL)),
    'metadata': pd.read_html(URL)[0].dropna(axis=0).to_dict()
}
print(data)
json_str = json.dumps(data) ####### 导出 json 写法不对，详见爬虫组聊天记录
with open(URL.split('/')[-1]+'.json', 'w') as json_file:
    json_file.write(json_str)
