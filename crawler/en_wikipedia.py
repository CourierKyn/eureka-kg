import requests
from bs4 import BeautifulSoup
import pprint
import re
import json
import pandas as pd

def get(url):
    try:
        return requests.get(url)
    except Exception as e:
        print(e, 'from', url)

def parse(r):
    if r is None:
        return
    soup = BeautifulSoup(r.text, 'lxml')
    name = soup.select('#firstHeading')
    description = soup.select('div.mw-parser-output > p')
    metadata = soup.select('div.mw-parser-output > table')[0]
    data = {'url': url,
    'name': name[0].get_text(),
    'description': description[0].get_text(),
    'metadata': pd.read_html(url)[0].dropna(axis=0).to_dict()
    }
    return data

url='https://en.wikipedia.org/wiki/Ant_Financial'
data=parse(get(url))
json_str = json.dumps(data)
with open(url.split('/')[-1]+'.json', 'w') as f:
    f.write(json_str，indent=4)
