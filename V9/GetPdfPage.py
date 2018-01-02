#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on Fri Dec 29 15:56:08 2017

马尔代夫V1.9

事情是这样的

之前的马尔代夫文章不保险

还有两天就要截稿了

我发现可以写个shortreport

但是找不到模板

有一系列pdf

我知道里面肯定有2页的

所以设计了这个程序帮我找到哪个pdf只有两页

@author: chunguang
"""

import os  
import glob  
from PyPDF2 import PdfFileReader

page = 2#指定需要pdf的页数

#获取指定目录下指定类型的文件
def open_allfile(path,filetype):  
    data=[]  
    read_files=glob.glob(path+'*'+filetype)  
    for i in read_files:  
        with open(i,'rb') as infile:  
            data.append(infile.read())  
    return data

#获得文件名，这里获得*.pdf的文件名
def get_filename(path,filetype):   
    name=[]  
    for root,dirs,files in os.walk(path):  
        for i in files:  
            if filetype in i:  
                #name.append(i.replace(filetype,'.pdf'))  
                name.append(i)  
    return name

#指定文件目录和文件类型
Mypath = 'E:/00000/Spyder_workspace/get_pdf_page/pdf'
Myfiletype = '.pdf'

#打开文件获得文件名 
Mydata = open_allfile(Mypath,Myfiletype)  
Myname = get_filename(Mypath,Myfiletype)  

#打印指定文件页数的文件名和页数
for respective_pname in Myname:
    # 获取一个 PdfFileReader 对象
    pdf_input = PdfFileReader(open('./pdf/' + respective_pname, 'rb'))
    # 获取 PDF 的页数
    page_count = pdf_input.getNumPages()
    if page_count == page:
            print(respective_pname)
            print(page_count)