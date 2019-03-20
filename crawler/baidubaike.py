
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import json


def get(url):
    try:
        return requests.get(url, headers={'user-agent': 'my-app/0.0.1'})
    except Exception as e:
        print(e, 'from', url)


def get_introduction(soup):
    
    if soup.select('p')[0].get_text() == '抱歉，您所访问的页面不存在...':
        return 0
    
    t = ''
    for i in soup.select("div.lemma-summary"):
        t += i.get_text()
    return t


def get_basic_info(soup):
    basic_info = {}
    try:
        for i in range(len(soup.select('div.basic-info')[0].select('dt'))) :
            basic_info[soup.select('div.basic-info')[0].select('dt')[i].get_text()
                      ] = soup.select('div.basic-info')[0].select('dd')[i].get_text()[1:-1]
    except IndexError:
        return np.nan
            
    return basic_info


def get_name(soup):
    return soup.select('div > dl > dd > h1')[0].string


def parse( url):
    if get(url) is None:
        return
    soup = BeautifulSoup(get(url).content.decode(), 'lxml')
    dic = {}
    dic['url'] = url
    dic['name'] = get_name(soup)
    dic['description'] = get_introduction(soup)
    dic['metadata'] = get_basic_info( soup)
    return dic


if __name__ == '__main__':

    url_list = ['https://baike.baidu.com/item/蚂蚁金服','https://baike.baidu.com/item/京东']
    
    for u in url_list:
        with open('百度百科.json','a', encoding='utf-8') as f:
            # 设置不转换成ascii  json字符串首缩进
            f.write( json.dumps( parse(u) ,ensure_ascii=False ,indent=2 ) )
        
 

