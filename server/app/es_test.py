# import pyes
# conn = pyes.ES(['127.0.0.1:9200'])#链接elasticsearch
# conn.create_index('test-index')#新建一个索引

from elasticsearch import Elasticsearch

es = Elasticsearch()
es.indices.create(index='news', ignore=400)
#删除数据
# result = es.indices.delete(index='news', ignore=[400, 404])
#更新数据
# data = {'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm', 'date': '2011-12-16'}
# result = es.update(index='news', doc_type='politics', body=data, id=1)
#添加数据
data = {'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm'}
result = es.create(index='news', doc_type='politics', id=1, body=data)
print(result)