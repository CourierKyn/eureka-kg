https://www.jianshu.com/p/1b750c4cd792  https://pyltp.readthedocs.io/zh_CN/latest/api.html #基于LTP的分句、分词、POS和依存句法分析的简单说明
https://github.com/HIT-SCIR/ltp #我们使用的开源nlp
https://blog.csdn.net/kevin_darkelf/article/details/39520881 #中文分词词性对照表##重要，我们要添加一些自己的字典###外部字典文件本身是一个文本文件，编码使用utf-8
关系类型说明见图片 关系类型.png
使用以下代码在命令行运行.py文件：
python fact_triple_extraction-master.py input.txt out_file_name.txt 
dict.txt为字典格式
最终的代码输出还未决定，当前版本的输出只是为了方便学习
需要修改.py文件33行的MODELDIR路径为你自己模型保存的路径，jupyter文件一样处理
data_analysis.py文件的功能为解析爬取得json格式文件，在命令行输入python data_analysis.py in_file_name.jsonlines
https://blog.csdn.net/Eastmount/article/details/50891162 #[python] LDA处理文档主题分布及分词、词频、tfidf计算##参考文章
lda_topic 文件中给了lda的示例，对每行文字进行聚类，topic_num列为聚类标签 #此代码有问题，有待解决
命令行运行 python lda_topic.py input_file_name n 第一个参数为输入的三元组文件名，第二个参数为聚类个数，目前输入过大的文件会出现MemoryError，有待解决。
推荐阅读技术文档，理解函数作用与内容
https://pyltp.readthedocs.io/zh_CN/latest/api.html#id10 pyltp官方技术文档
http://www.ltp-cloud.com/intro#ltp_cloud ltp官方技术文档
