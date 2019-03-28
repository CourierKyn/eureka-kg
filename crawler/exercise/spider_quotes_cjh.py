#为了方便看，我的备注就写这里了
##选取下一页的时候不要用 sub_soup.select(' nav > ul > li > a') ，用 soup.select('li.next') ，就不需要判断是否有上一页，则第一页和第二页就不用分开处理
##get_text,get_author,get_tag 的时候有可能返回一个空列表，需要进行处理，如填充0 或者NA

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import Series,DataFrame


url = "http://quotes.toscrape.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
df = DataFrame()


def get_text(sub_soup):
    text = [i.get_text()[1:-1] for i in sub_soup.select("span.text")]
    return text[0]


def get_author(sub_soup):
    author =  [i.get_text() for i in sub_soup.select("small")]
    return author[0]


def get_tag(sub_soup):
    tag = [i['content'] for i in sub_soup.select("div > meta")]
    return tag


def get_next_pages_beautifulSoup(sub_soup, button, start_url):
    url = start_url + sub_soup.select(' nav > ul > li > a')[button]['href'][1:]
    print(url)
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    return soup


def combine_information(text, author, tag, dafr):
    df = pd.concat([dafr,DataFrame({'text':text,'author':author,'tag':tag})],ignore_index=True)
    return df


def get_block_information(sub_soup, df):
    for i in sub_soup.select("div.quote"):
        text = get_text(i)
        tag = get_tag(i)
        author = get_author(i)
        
        df = combine_information(text, author, tag, df)
    return df


# ## 先get第一页


df = get_block_information(soup, df)


# ## 因为第一页没有“前一页”，去下一页的按钮的位置不同，还要写一遍get第二页。




soup = get_next_pages_beautifulSoup(soup,0,url)
df = get_block_information(soup, df)


# ## 然后就可以开开心心地用循环了



try:
    while soup.select(' nav > ul > li > a')[1].get_text() == 'Next →':
        
        df = get_block_information(soup, df)
        soup = get_next_pages_beautifulSoup(soup,1, url)
except IndexError:
    print('done')
    
df

