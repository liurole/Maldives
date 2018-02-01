# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

"""

import xlrd  
import difflib
import re

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

def separated(id):
    tables = excel_table_byindex('总结.xlsx', 0, id)
    name = []
    name.append(tables[0]['厂牌'])
    for i in range(1, len(tables)):
        ratio = 1
        temp = tables[i]['厂牌']
        temp = re.sub('[^a-zA-Z\s]', '', temp).lower()
        for val in name:
            ratio = compare_str(val, temp)
        if ratio < 0.8:
            name.append(temp)
    return name
            

# 帮助run Maldives5.2.0.py --help
if __name__ == '__main__':
    
    factory = []
    names = []
    
    
    
    
    types =[]
    sizes = []
    # 查找index
    with open("detail.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            temp = row['型号']
            temp_list = temp.split('-')
            temp = ''
            for i in range(len(temp_list) - 1):
                if i == 0:
                    temp += temp_list[i]
                else:
                    temp += '-' + temp_list[i]
            types.append(temp)
            temp = row['Outer Dimension (mm):']
            sizes.append(temp)            
            
    type_id = 0
    type_store = []
    for i, val in enumerate(types):
        if i == 0:
            type_store.append(type_id)
        else:
            ratio1 = compare_str(types[i - 1], types[i])
            ratio2 = compare_str(sizes[i - 1], sizes[i])
            if ratio1 < 0.85 or ratio2 < 0.98:
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