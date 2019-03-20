https://www.jianshu.com/p/1b750c4cd792  https://pyltp.readthedocs.io/zh_CN/latest/api.html #基于LTP的分句、分词、POS和依存句法分析的简单说明
https://github.com/HIT-SCIR/ltp #我们使用的开源nlp
https://blog.csdn.net/kevin_darkelf/article/details/39520881 #中文分词词性对照表##重要，我们要添加一些自己的字典###外部字典文件本身是一个文本文件，编码使用utf-8
关系类型说明见图片 关系类型.png
使用以下代码在命令行运行.py文件：
python fact_triple_extraction-master.py input.txt out_file_name.txt 
dict.txt为字典格式
最终的代码输出还未决定，当前版本的输出只是为了方便学习