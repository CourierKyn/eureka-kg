# by 阿镇

from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series,DataFrame

def fetchAndParse(URL): ######## 使用 try except 语句
    try:
        soup = BeautifulSoup(requests.get(URL).text,'lxml')
        return soup
    except:
        print('RequestException from index page')
        return None

def findContentAndRebuildDf(soup):
    for sub_soup in soup.select('div.quote'): ######### 将 i 改名为 sub_soup
        if len(sub_soup.select('span.text')) != 0:
             text = sub_soup.select('span.text')[0].get_text()[1:-1]
        if len(sub_soup.select('small.author')) != 0:
             author = sub_soup.select('small.author')[0].get_text()
        if len(sub_soup.select('meta.keywords')) != 0:
             tag = sub_soup.select('meta.keywords')[0].get('content')

        df_new = pd.DataFrame( ########## 若 select 为空列表，则会出现 IndexError，需进行处理
            [[text,author,tag]],
            columns=['text','author','tag'])
        global df
        df = pd.concat([df,df_new],ignore_index=True)
    return df

def getNextPage(soup):
    if len(soup.select('li.next')) != 0:
        return URL + soup.select('li.next')[0].select('a')[0].get('href')[1:]

def main(URL):
    while True:
        soup = fetchAndParse(URL)
        df = findContentAndRebuildDf(soup)
        _ = getNextPage(soup)
        if _:
            URL = _
        else:
            break
    return df ########## 应将结果写入到文件中，如 json、csv

if __name__ == '__main__':
    URL = "http://quotes.toscrape.com/" ######## 这两行放到最后面 if __name__ == '__main__' 里面
    df = pd.DataFrame(columns=['text','author','tag'])
    print(main(URL)) ######## 最后一行空行
