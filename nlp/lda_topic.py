
# coding: utf-8

# In[16]:


# coding=utf-8         
import os  
import sys
import pandas as pd
import numpy as np
import matplotlib
import scipy
import matplotlib.pyplot as plt
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer 
import lda
import lda.datasets


# In[17]:


input_file_name = sys.argv[1]
n = int(sys.argv[2])


# In[12]:


#存储读取语料 一行语料为一个文档 
def load_file(input_file_name): 
    '''输入文件为三元组文件'''
#    in_file='data/out_file/'+input_file_name+'.txt'
    in_file=input_file_name+'.txt'
    corpus =[line.strip() for line in open(in_file, 'r',encoding='utf-8').readlines()]
    return corpus


# In[18]:


#将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
# def change_to_wfm(corpus):#wfm全称word frequency matrix
#     vectorizer = CountVectorizer(corpus)
#     print(vectorizer)

#     X = vectorizer.fit_transform(corpus)
#     analyze = vectorizer.build_analyzer()
#     weight = X.toarray()
 
#     print(len(weight))
#     print(weight[:5, :5])
#     return weight


# In[5]:


def read_csv(input_file_name):
    input_file_name=input_file_name+'.txt'
    data=pd.read_csv(input_file_name,header=None)
    data.columns=['object','relation','subject']
    return data


# In[9]:


def lda_clust(corpus,data,n):
    vectorizer = CountVectorizer(corpus)
    print(vectorizer)

    X = vectorizer.fit_transform(corpus)
    analyze = vectorizer.build_analyzer()
    weight = X.toarray()
 
    print(len(weight))
    print(weight[:5, :5])
    model = lda.LDA(n_topics=n, n_iter=500, random_state=1)
    model.fit(np.asarray(weight))    # model.fit_transform(X) is also available
    topic_word = model.topic_word_    # model.components_ also works
    doc_topic = model.doc_topic_
    data['topic_num']=np.nan
    for n in range(0,doc_topic.shape[0]):
        topic_most_pr = doc_topic[n].argmax()
        data.iloc[n,3]=int(topic_most_pr)
#         print("doc: {} topic: {}".format(n, topic_most_pr))
    data=data.set_index('topic_num')
    return data


# In[13]:


def to_csv(output_file_name,data):
    data.to_csv(output_file_name)


# In[14]:


def main(input_file_name,n):
    corpus=load_file(input_file_name)
    data=read_csv(input_file_name)
    data=lda_clust(corpus,data,n)
    output_file_name=input_file_name+'_clust.txt'
    to_csv(output_file_name,data)


# In[ ]:


if __name__=='__main__':
    main(input_file_name,n)

