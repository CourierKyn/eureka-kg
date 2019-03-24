
# coding: utf-8

# In[52]:


#!/usr/bin/env python
# coding=utf-8
"""
文本中事实三元组抽取
python *.py input.txt output.txt begin_line end_line
"""
# 原作者
__author__ = "tianwen jiang"
# 原代码版本为Python2.7
# 以下代码运行在Python3.6
# 大部分注释是我自己加的，不一定准确


# In[53]:


import sys
import os
from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer# 需装Python后再下载模型，此次运行的模型版本为3.4.0


# In[54]:


print("正在加载LTP模型... ...")
# Set your own model path
MODELDIR="E:\pyltp_model\ltp_data_v3.4.0"

segmentor = Segmentor()
cws_model_path=os.path.join(MODELDIR, "cws.model")
segmentor.load_with_lexicon(cws_model_path, './dict.txt') #请把字典文件放进当前文件夹
#segmentor.load(os.path.join(MODELDIR, "cws.model"))

postagger = Postagger()
postagger.load(os.path.join(MODELDIR, "pos.model"))

parser = Parser()
parser.load(os.path.join(MODELDIR, "parser.model"))

recognizer = NamedEntityRecognizer()
recognizer.load(os.path.join(MODELDIR, "ner.model"))

#labeller = SementicRoleLabeller()
#labeller.load(os.path.join(MODELDIR, "srl/"))

print("加载模型完毕。")


# In[55]:


# in_file_name = "in_file.txt"# 输入你想要抽取三元组的文件
# out_file_name = "out_file.txt"# 保存三元组文件
begin_line = 1
end_line = 0


# In[56]:


if len(sys.argv) > 1:
    in_file_name = sys.argv[1]

if len(sys.argv) > 2:
    out_file_name = sys.argv[2]

if len(sys.argv) > 3:
    begin_line = int(sys.argv[3])

if len(sys.argv) > 4:
    end_line = int(sys.argv[4])


# In[57]:


def extraction_start(in_file_name, out_file_name, begin_line, end_line):
    """
    事实三元组抽取的总控程序
    Args:
        in_file_name: 输入文件的名称
        #out_file_name: 输出文件的名称
        begin_line: 读文件的起始行
        end_line: 读文件的结束行
    """
    in_file = open(in_file_name, 'r', encoding='utf-8')
    out_file = open(out_file_name, 'a', encoding='utf-8')
    
    line_index = 1
    sentence_number = 0
    text_line = in_file.readline() # 读取一行
    while text_line:
        # 读取下一行----------------------------
        if line_index < begin_line:
            text_line = in_file.readline()
            line_index += 1
            continue
        if end_line != 0 and line_index > end_line:
            break
        sentence = text_line.strip()
        # --------------------------------------
        if sentence == "" or len(sentence) > 1000: # 不读取空行和长度超过1000的行
            text_line = in_file.readline()
            line_index += 1
            continue
        try:
            fact_triple_extract(sentence, out_file) 
            out_file.flush() #把缓冲区的文件强制写出，这里可能可以优化
        except:
            pass
        sentence_number += 1
        if sentence_number % 50 == 0:
            print("完成50个句子的抽取")
        text_line = in_file.readline()
        line_index += 1
    in_file.close()
    out_file.close()


# In[58]:


def fact_triple_extract(sentence, out_file):
    """
    对于给定的句子进行事实三元组抽取
    Args:
        sentence: 要处理的语句
    """
    # 切割句子
    words = segmentor.segment(sentence)
    # 词性标注
    postags = postagger.postag(words)
    # 命名实体识别
    netags = recognizer.recognize(words, postags)
    # 依存句法分析，其中已有模型可将句子中的主谓宾等结构抽取出来
    arcs = parser.parse(words, postags)

    child_dict_list = build_parse_child_dict(words, postags, arcs)
    for index in range(len(postags)):
        # 抽取以谓词为中心的事实三元组
        if postags[index] == 'v':
            child_dict = child_dict_list[index]
            # 主谓宾
            if   ('SBV') in child_dict and  ('VOB') in child_dict:
                e1 = complete_e(words, postags, child_dict_list, child_dict['SBV'][0])
                r = words[index]
                e2 = complete_e(words, postags, child_dict_list, child_dict['VOB'][0])
                out_file.write("%s, %s, %s\n" % (e1, r, e2)) #此处三元组的输出格式有待规范
                out_file.flush()
            # 定语后置，动宾关系
            if arcs[index].relation == 'ATT':
                if  ('VOB') in child_dict:
                    e1 = complete_e(words, postags, child_dict_list, arcs[index].head - 1)
                    r = words[index]
                    e2 = complete_e(words, postags, child_dict_list, child_dict['VOB'][0])
                    temp_string = r+e2
                    if temp_string == e1[:len(temp_string)]:
                        e1 = e1[len(temp_string):]
                    if temp_string not in e1:
                        out_file.write("%s, %s, %s\n" % (e1, r, e2)) #此处三元组的输出格式有待规范
                        out_file.flush()
            # 含有介宾关系的主谓动补关系
            if  ('SBV') in child_dict and  ('CMP') in child_dict:
                #e1 = words[child_dict['SBV'][0]]
                e1 = complete_e(words, postags, child_dict_list, child_dict['SBV'][0])
                cmp_index = child_dict['CMP'][0]
                r = words[index] + words[cmp_index]
                if  ('POB') in child_dict_list[cmp_index]:
                    e2 = complete_e(words, postags, child_dict_list, child_dict_list[cmp_index]['POB'][0])
                    out_file.write("%s, %s, %s\n" % (e1, r, e2)) #此处三元组的输出格式有待规范
                    out_file.flush()

        # 尝试抽取命名实体有关的三元组
        if netags[index][0] == 'S' or netags[index][0] == 'B':
            ni = index
            if netags[ni][0] == 'B':
                while netags[ni][0] != 'E':
                    ni += 1
                e1 = ''.join(words[index:ni+1])
            else:
                e1 = words[ni]
            if arcs[ni].relation == 'ATT' and postags[arcs[ni].head-1] == 'n' and netags[arcs[ni].head-1] == 'O':
                r = complete_e(words, postags, child_dict_list, arcs[ni].head-1)
                if e1 in r:
                    r = r[(r.index(e1)+len(e1)):]
                if arcs[arcs[ni].head-1].relation == 'ATT' and netags[arcs[arcs[ni].head-1].head-1] != 'O':
                    e2 = complete_e(words, postags, child_dict_list, arcs[arcs[ni].head-1].head-1)
                    mi = arcs[arcs[ni].head-1].head-1
                    li = mi
                    if netags[mi][0] == 'B':
                        while netags[mi][0] != 'E':
                            mi += 1
                        e = ''.join(words[li+1:mi+1])
                        e2 += e
                    if r in e2:
                        e2 = e2[(e2.index(r)+len(r)):]
                    if r+e2 in sentence:
                        out_file.write("%s, %s, %s\n" % (e1, r, e2)) #此处三元组的输出格式有待规范
                        out_file.flush()


# In[59]:


def build_parse_child_dict(words, postags, arcs):
    """
    为句子中的每个词语维护一个保存句法依存儿子节点的字典
    Args:
        words: 分词列表
        postags: 词性列表
        arcs: 句法依存列表
    """
    child_dict_list = []
    for index in range(len(words)):
        child_dict = dict()
        for arc_index in range(len(arcs)):
            if arcs[arc_index].head == index + 1:
#                 if child_dict.has_key(arcs[arc_index].relation):
                if (arcs[arc_index].relation) in child_dict:
                    child_dict[arcs[arc_index].relation].append(arc_index)
                else:
                    child_dict[arcs[arc_index].relation] = []
                    child_dict[arcs[arc_index].relation].append(arc_index)
        if ('SBV') in child_dict:
            print(words[index],child_dict['SBV'])
        child_dict_list.append(child_dict)
    return child_dict_list


# In[60]:


def complete_e(words, postags, child_dict_list, word_index):
    """
    完善识别的部分实体
    """
    child_dict = child_dict_list[word_index]
    prefix = ''
    if ('ATT') in child_dict:
        for i in range(len(child_dict['ATT'])):
            prefix += complete_e(words, postags, child_dict_list, child_dict['ATT'][i])
    
    postfix = ''
    if postags[word_index] == 'v':
        if ('VOB') in child_dict:
            postfix += complete_e(words, postags, child_dict_list, child_dict['VOB'][0])
        if ('SBV') in child_dict:
            prefix = complete_e(words, postags, child_dict_list, child_dict['SBV'][0]) + prefix

    return prefix + words[word_index] + postfix


# In[61]:


if __name__ == "__main__":
    #extraction_start(in_file_name, out_file_name, begin_line, end_line)
    extraction_start(in_file_name, out_file_name, begin_line, end_line)

