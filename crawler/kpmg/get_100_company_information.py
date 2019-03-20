import re
import json
from get100CompanyName import pdfCrap

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser, PDFDocument

def parsePDFToList(path):
    '''
    把pdf文件的每一页分别装换成txt并储存在一个列表里面
    :param path: 输入的pdf文件
    :return:
    '''
    text = []
    with open(path,'rb')as fp:# rb以二进制读模式打开本地pdf文件

        # 用文件对象来创建一个pdf文档分析器
        praser_pdf = PDFParser(fp)
        # 创建一个PDF文档
        doc = PDFDocument()

        # 连接分析器 与文档对象
        praser_pdf.set_document(doc)
        doc.set_parser(praser_pdf)

        # 提供初始化密码doc.initialize("123456")
        # 如果没有密码 就创建一个空的字符串
        doc.initialize()

        # 检测文档是否提供txt转换，不提供就忽略
        if not doc.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            # 创建PDf资源管理器 来管理共享资源
            rsrcmgr = PDFResourceManager()

            # 创建一个PDF参数分析器  创建一个PDF设备对象
            laparams = LAParams()

            # 创建聚合器
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)

            # 创建一个PDF页面解释器对象
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            # 循环遍历列表，每次处理一页的内容
            # doc.get_pages() 获取page列表
            for page in doc.get_pages():
                # 使用页面解释器来读取
                interpreter.process_page(page)

                # 使用聚合器获取内容
                layout = device.get_result()
                results1 = ''
                for out in layout:
                    if isinstance(out, LTTextBoxHorizontal):
                        results = out.get_text()
                        results1 = results1 + results
                text.append(results1)
    return text

def get50LeadingCompanyInformation(text):
    patternOfName = re.compile(r'\d\d\n(.+)\n')
    patternOfDescription = re.compile(r'At a Glance\n([\s\S]+)\nNotable Investors')
    patternOfYear = re.compile(r'Year Founded  \n(.+)\n')
    patternOfLocation = re.compile(r'Located  \n(.+)\n')
    patternOfWebsite = re.compile(r'Website  \n(.+)\n')
    patternOfCategory = re.compile(r'Category  \n(.+)')
    patternOfOwnership  = re.compile(r'Ownership  \n(.+)')
    patternOfKeyPeople = re.compile(r'Key People  \n([\s\S]+)\nWebsite')
    patternOfInvestors = re.compile(r'Notable Investors\n([\s\S]+)\nCategory')
    try:
        Name = patternOfName.findall(text)[0]
    except:
        Name =None
    try:
        Description = re.sub(r'\n',"",patternOfDescription.findall(text)[0])
    except:
        Description = None
    try:
        Year = patternOfYear.findall(text)[0]
    except:
        Year = None
    try:
        Location = patternOfLocation.findall(text)[0]
    except:
        Location = None
    try:
        Website = patternOfWebsite.findall(text)[0]
    except:
        Website = None
    try:
        Category = patternOfCategory.findall(text)[0]
    except:
        Category = None
    try:
        Ownership = patternOfOwnership.findall(text)[0]
    except:
        Ownership = None
    try:
        Keypeople = re.sub(r'\n',",",patternOfKeyPeople.findall(text)[0])
    except:
        Keypeople = None
    try:
        Investors = re.sub(r'\n',"",patternOfInvestors.findall(text)[0])
    except:
        Investors = None
    Information = {'Name': Name,'Description': Description,'Year': Year,'Location': Location,'Website': Website,'Category':Category,'Ownership':Ownership,'Keypeople':Keypeople,'Investors':Investors}
    return Information

def get50EmergingCompanyInformation(text):
    patternOfName = re.compile(r'\ue801\n(.+)\n')
    patternOfDescription = re.compile(r'At a Glance\n([\s\S]+)\nNotable Investors')
    patternOfYear = re.compile(r'Year Founded  \n(.+)\n')
    patternOfLocation = re.compile(r'Located  \n(.+)\n')
    patternOfWebsite = re.compile(r'Website  \n(.+)\n')
    patternOfCategory = re.compile(r'Category  \n(.+)')
    patternOfOwnership  = re.compile(r'Ownership  \n(.+)')
    patternOfKeyPeople = re.compile(r'Key People  \n([\s\S]+)\nWebsite')
    patternOfInvestors = re.compile(r'Notable Investors\n([\s\S]+)\nCategory')
    try:
        Name = patternOfName.findall(text)[0]
    except:
        Name =None
    try:
        Description = re.sub(r'\n',"",patternOfDescription.findall(text)[0])
    except:
        Description = None
    try:
        Year = patternOfYear.findall(text)[0]
    except:
        Year = None
    try:
        Location = patternOfLocation.findall(text)[0]
    except:
        Location = None
    try:
        Website = patternOfWebsite.findall(text)[0]
    except:
        Website = None
    try:
        Category = patternOfCategory.findall(text)[0]
    except:
        Category = None
    try:
        Ownership = patternOfOwnership.findall(text)[0]
    except:
        Ownership = None
    try:
        Keypeople = re.sub(r'\n',",",patternOfKeyPeople.findall(text)[0])
    except:
        Keypeople = None
    try:
        Investors = re.sub(r'\n',"",patternOfInvestors.findall(text)[0])
    except:
        Investors = None
    Information = {'Name': Name,'Description': Description,'Year': Year,'Location': Location,'Website': Website,'Category':Category,'Ownership':Ownership,'Keypeople':Keypeople,'Investors':Investors}
    return Information

if __name__ == '__main__':
    pdfCrap(r"Fintech100-2018-Report_Final_22-11-18sm.pdf",12,100,r"Fintech100-12-111.pdf")
    text = parsePDFToList(r"Fintech100-12-111.pdf")
    Company100Information = []
    a = 0
    for i in text[0:50]:
        a += 1
        Company100Information.append(get50LeadingCompanyInformation(i))
        print(a)
    for i in text[50:100]:
        a += 1
        Company100Information.append(get50EmergingCompanyInformation(i))
        print(a)
    with open('Company100Information.json', 'w') as f:
            json.dump(Company100Information, f, indent=4)