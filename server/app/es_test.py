# import pyes
# conn = pyes.ES(['127.0.0.1:9200'])#链接elasticsearch
# conn.create_index('test-index')#新建一个索引

from elasticsearch import Elasticsearch
import json
import re
data = [json.loads(line) for line in open('data/iotworm.jsonlines')]
es = Elasticsearch()
es.indices.create(index='news', ignore=400)
#删除数据
# result = es.indices.delete(index='news', ignore=[400, 404])
#更新数据
# data = {'title': 'for update', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm', 'date': '2011-12-16'}
# result = es.update(index='news', doc_type='politics', body=data, id=1)
#添加数据
# i = 1
# for d in data:
#     result = es.create(index='news', doc_type='politics', id=i, body=d)
#     i+=1
#     print(result)
#查询
dsl = {
    'query': {
        'match': {
            'summary': 'iot fintech'
        }
    }
}
result = es.search(index='news', doc_type='politics',body=dsl)
print(json.dumps(result, sort_keys=True, indent=4))#json格式化输出

