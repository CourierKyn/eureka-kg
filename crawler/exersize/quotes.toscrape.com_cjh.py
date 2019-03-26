####### 去掉下面这些 jupyter 生成的注释
# coding: utf-8

# In[1]:


from urllib.request import urlopen ######### 用 requests，见群里发的文档
from bs4 import BeautifulSoup
import re
import pandas as pd
from pandas import Series,DataFrame


# In[2]:


html = urlopen('http://quotes.toscrape.com/')
bs = BeautifulSoup(html, "html.parser") ###### 命名为 soup，与官方文档保持一致，下同
df = DataFrame()


# In[3]:


df


# In[4]:


def get_text(bs): ####### 参数命名为 sub_soup
    text = [i.get_text()[1:-1] for i in bs.select("span.text")]
    return text ####### 返回 str 而不是 [str]，下同


# In[5]:


def get_author(bs):
    author = [i.get_text() for i in bs.select("small")]
    return author


# In[6]:


def get_tag(bs):
    tag = [i['content'] for i in bs.select("div > meta")]
    return tag


# In[7]:


def next_pages_beautifulSoup(bs, bottom): ######## 函数命名 get_..._... 与其他函数保持一致
                                          ######## url 作为参数传入，而不是在函数内生成
    url = "http://quotes.toscrape.com/" + bs.select(' nav > ul > li > a')[bottom]['href'][1:]
    print(url)
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser") ######## 使用 lxml 而不是速度更慢的 html.parser
    return bs


# In[8]:


def combine_information(text, author, tag,dafr):
    df = pd.concat([dafr,DataFrame({'text':text,'author':author,'tag':tag})],ignore_index=True)
    return df


# ## 先get第一页

# In[9]:


text1 = get_text(bs)
tag1 = get_tag(bs)
author1 = get_author(bs)
df = combine_information(text1, author1,tag1,df)


# ## 因为第一页没有“前一页”，去下一页的按钮的位置不同，还要写一遍get第二页。。。

# In[10]:


bs = next_pages_beautifulSoup(bs,0)
text2 = get_text(bs)
tag2 = get_tag(bs)
author2 = get_author(bs)
df = combine_information(text2, author2,tag2,df)


# ## 然后就可以开开心心地用循环了

# In[11]:


try:
    while bs.select(' nav > ul > li > a')[1].get_text() == 'Next →': ######### 直接 select next 按钮，没找到就 break
            text = get_text(bs)
            author = get_author(bs)
            tag = get_tag(bs)

            df = combine_information(text, author, tag,df)

            bs = next_pages_beautifulSoup(bs,1)
except IndexError:
    print('done')
    
df

