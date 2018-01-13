# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

马尔代夫V5.4.0

实现了同类产品大小型号的合并

"""

import sys
import getopt
import csv
import codecs
import difflib
import xlrd 

def compare_str(first, second):
    seq = difflib.SequenceMatcher(lambda x: x in '-', first, second)  
    ratio = seq.ratio()
    return ratio    

def open_excel(file):  
    data = xlrd.open_workbook(file)  
    return data

def excel_table_byindex(file, colnameindex = 0, by_index = 0):  
    data = open_excel(file)  
    table = data.sheets()[by_index]  
    nrows = table.nrows #行数   
    colnames = table.row_values(colnameindex) #某一行数据  
    list = []  
    for rownum in range(1,nrows):  
        row = table.row_values(rownum)#以列表格式输出  
        if row:  
            app = {}  
            for i in range(len(colnames)):  
                app[colnames[i]] = row[i]  
            list.append(app)#向列表中插入字典类型的数据  
    return list 

# 帮助run Maldives5.4.0.py --help
if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hi:', [ 'help' ])
    
    # 入口函数
    for key, value in opts:
        if key in ['-h', '--help']:
            print('马尔代夫V5.4.0')
            print('参数定义：')
            print('-h, --help\t实现了同类产品大小型号的合并')
            sys.exit(0)    
    
    tables = excel_table_byindex('detail.xlsx', 0, 3) 
    
    types =[]
    sizes = []
    
    for row in tables:
        types.append(row['型号'])
        sizes.append(row['Size'])   
            
    type_id = 0
    type_store = []
    for i, val in enumerate(types):
        if i == 0:
            type_store.append(type_id)
        else:
            ratio1 = compare_str(types[i - 1], types[i])
            ratio2 = compare_str(sizes[i - 1], sizes[i])
            if ratio1 < 0.8 or ratio2 < 0.98:
                type_id += 1
            type_store.append(type_id)
                
    with codecs.open('大小型号归类.csv',"w",'utf_8_sig') as f:
        writer_a = csv.writer(f)
        for i, val in enumerate(types):
            row = []
            row.append(val)
            row.append(type_store[i])
            writer_a.writerow(row)
        f.close()         