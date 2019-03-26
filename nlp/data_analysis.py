
# coding: utf-8

# In[2]:


import json
from bs4 import BeautifulSoup
import sys


# In[3]:


input_file = sys.argv[1]


# In[4]:


def data_analysis(input_file):
    data = [json.loads(line) for line in open('data/jsondata/'+str(input_file)+'.jsonlines')] #加载文件
    file=''.join((BeautifulSoup(f['summary'],'lxml').get_text() for f in data)) #解析json文件
    #写入文件---------------------------------------------------------------------------
    file_handle=open('data/utf_8data/'+str(input_file)+'.txt',mode='w',encoding='utf-8')
    file_handle.write(file)
    file_handle.close
    #-----------------------------------------------------------------------------------


# In[ ]:


if __name__ =='__main__':
    data_analysis(input_file)

