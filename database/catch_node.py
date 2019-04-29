import re
import pandas as pd
f=open("D:\pyhton\Scripts\output.txt",encoding='utf-8')
file=f.read()
searchObj = re.findall( r'\t\S(.*), (.*), (.*)\S\n',file, re.M|re.I)#使用正则表达式，分成诗名、诗人、诗句三个内容
searchObj=pd.DataFrame(searchObj,columns=['主语','谓语','宾语'])#转换成Dataframe