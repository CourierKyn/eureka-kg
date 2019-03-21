#!/usr/bin/env python
# coding: utf-8

# In[123]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import json
from pandas.io.json import json_normalize
import pprint
import requests


def get(url):
    try:
        proxies = {"http": "http://68.183.34.61",}
        html=requests.get(url, proxies=proxies).text
        return html
    except Exception as e:
        print(e, 'from', url)

def parse(html):
    try:
        pre_text=BeautifulSoup(html,'lxml')
        [c.extract() for c in pre_text('sup')]
        company={'URL':url,
                 'name':pre_text.select('.firstHeading')[0].get_text(),
                 'description':pre_text.select('.mw-parser-output > p ')[0].get_text(),
                 'metadata':pd.read_html(html)[0].dropna(axis=0).to_dict()}
        return company
    except Exception as e:
        print(e, 'from', url)   
    
    
    
    

if __name__ == '__main__':
    url="https://zh.wikipedia.org/zh-cn/蚂蚁金服"
#     get(url)
    out=parse(get(url))
    pprint.pprint(out)
with open('out.json', 'w') as f:
        json.dump(out, f, indent=4)

