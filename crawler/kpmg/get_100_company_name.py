import sys
import re
import json

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser, PDFDocument

from PyPDF2 import PdfFileWriter, PdfFileReader

def  pdfCrap(path,start_page,i,save_path):
    """
    从pdf文件中截取几页，并保存在对应pdf文件中
    """
    # 开始页
    start_page = start_page - 1
    # 截止页
    end_page = start_page +  i  # 这里设定截取几页
    output = PdfFileWriter()
    pdf_file = PdfFileReader(open(path, "rb"), strict=False)
    pdf_pages_len = pdf_file.getNumPages()
    for i  in  range(start_page, end_page):
        output.addPage(pdf_file.getPage(i)) # 在输出流中添加页
    outputStream =  open(save_path, "wb")
    output.write(outputStream)

def parse(path,text):
    '''
    将pdf转换成txt

    :param path: 输入的pdf文件
    :param text: 输出的txt文件
    '''
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

                # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
                for out in layout:
                    # 判断是否含有get_text()方法，图片之类的就没有
                    # if hasattr(out,"get_text"):
                    if isinstance(out, LTTextBoxHorizontal):
                        results = out.get_text()
                        text.write(results)

if __name__ == '__main__':
    PathOfOriginalPDF = r"Fintech100-2018-Report_Final_22-11-18sm.pdf"
    PathOfModifiedPDF = r"Fintech100-10-11.pdf"
    pdfCrap(PathOfOriginalPDF, 10,2,PathOfModifiedPDF)
    with open('text_10_11.txt', 'wt', encoding='utf-8') as text:
        parse(PathOfModifiedPDF, text)

    text = open(r"text_10_11.txt", 'r', encoding='utf-8').read()
    patternOfLeading_50 = re.compile(r'#\d\d (.+)')
    patternOfEmerging_50 = re.compile(r'\ue801 ([\s\S]+?)(?=\n[^a-zA-z])')
    Leading_50 = patternOfLeading_50.findall(text)
    Emerging_50 = patternOfEmerging_50.findall(text)
    print('获取到的公司数：',len(Leading_50)+len(Emerging_50))
    if len(Leading_50)+len(Emerging_50) == 100:
        with open('Company100.json', 'w') as f:
            json.dump({'Leading_50': Leading_50, 'Emerging_50': Emerging_50}, f, indent=4)