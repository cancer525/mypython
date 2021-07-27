from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import logging

def extract_pdf_content(pdf_path):
    rsrcmgr = PDFResourceManager()
    codec = 'utf-8'
    outfp = StringIO()#开始捕捉字节流(outfp)
    laparams = LAParams()
    device = TextConverter(rsrcmgr=rsrcmgr, outfp=outfp, codec=codec, laparams=laparams)
    with open(pdf_path, 'rb') as fp:#将pdf文件转换为二进制数据
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)#解析pdf的每一页，以二进制数据缓存
    mystr = outfp.getvalue()#捕获二进制信息流，以字符串的形式返回
    device.close()
    outfp.close()
    return mystr

import os
import glob

def geturlPath(year):
    path = r"C:\\Users\\Shayla\\Desktop\\ani".format(year)
    pdfs = glob.glob("{}/*.pdf".format(path))
    return pdfs

def record(file_path):
    #create logger
    logger = logging.getLogger("PDF-miner")
    logger.setLevel(logging.DEBUG)
    #create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    #crate formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #add formatter to ch
    ch.setFormatter(formatter)
    #add ch to logger
    logger.addHandler(ch)
    #application code
    info = "已解析完{}".format(file_path)
    logger.info(info)
    logging.basicConfig(filename=r'C:\\Users\\Shayla\\Desktop\\pdftotxt.txt',level=logging.DEBUG,encoding='utf-8')
    print(logger.info(info))


#from pdf_to_txt import *
import pandas as pd
from pandas import *

pdf_paths = geturlPath(2010)

def get_txt(pdf_paths):
    mydict = {}

    for pdf_path in pdf_paths:
        key = pdf_path.split("\\")[-1]
        print("*"*25,"正在提取{}的内容".format(key),"*"*25)
        mystr = extract_pdf_content(pdf_path)
        record(key)
        mydict[key] = mystr

    df_Economist = pd.DataFrame.from_dict(mydict,orient="index").reset_index()
    df_Economist.columns = ["path","content"]

    return df_Economist
get_txt(pdf_paths)