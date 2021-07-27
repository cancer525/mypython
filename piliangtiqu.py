import pandas as pd
import os
import glob
from pathlib import Path
from pdfminer.pdfinterp import PDFPageInterpreter,PDFResourceManager
from pdfminer.converter import TextConverter,PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfpage import PDFPage

dirPath=glob.iglob('C:\\Users\\Shayla\\Desktop\\重要')
for file in dirPath:
    files=os.listdir(file)
    print(files)
    print(len(files))
p=Path("C:\\Users\\Shayla\\Desktop\\重要")
filelist=list(p.glob("*.pdf"))

for file in filelist:
    fp=open(file,'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser=parser)
    parser.set_document(doc=doc)
    resource = PDFResourceManager()
    laparam=LAParams()
    device = PDFPageAggregator(resource,laparams=laparam)
    interpreter = PDFPageInterpreter(resource,device)
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        layout = device.get_result()
        for out in layout:
            if hasattr(out,'get_text'):
                print(out.get_text())
                fw = open('C:\\Users\\Shayla\\Desktop\\重要\\7.txt','a',encoding='utf-8')
                fw.write(out.get_text())