# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

"""

import xlrd  
import difflib
import re

# 比较字符串
def compare_str(first, second):
    seq = difflib.SequenceMatcher(lambda x: x in '-', first, second)  
    ratio = seq.ratio()
    return ratio    

# 读取excel
def open_excel(file):  
    data = xlrd.open_workbook(file)  
    return data

# 读取excel
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

# 获取单个表的厂牌，姓名
def separatedfactory(id, th1, th2):
    tables = excel_table_byindex('总结.xlsx', 0, id)
    factory = []
    name = []
    init = 1
    for i in range(len(tables)):
        ratio_f = 0
        ratio_n = 0
        temp_f = tables[i]['厂牌']
        temp_n = tables[i]['姓名']
        if '翻译' in temp_n:
            temp_n = temp_n[:-4]
        temp_f = re.sub('[^a-zA-Z\s]', '', temp_f).lower()
        if temp_f == '':
            continue
        if init:
            factory.append(temp_f)
            name.append(temp_n)
            init = 0
        else:
            for val in factory:
                r = compare_str(val, temp_f)
                ratio_f = max(ratio_f, r)
            if ratio_f < th1:
                factory.append(temp_f)
            for val in name:
                r = compare_str(val, temp_n)
                ratio_n = max(ratio_n, r)
            if ratio_n < th2:
                name.append(temp_n)
    return (factory, name)

# 获取所有厂牌
def allfactory(total, th1, th2):
    totalfactory = []
    totalname = []
    init_f = 1
    init_n = 1
    for i in range(total):
        temp_f, temp_n = separatedfactory(i, th1, th2)
        for val in temp_f:
            ratio_f = 0
            if init_f:
                totalfactory.append(val)
                #print(val)
                init_f = 0
            else:
                for j in totalfactory:
                    r = compare_str(j, val)
                    ratio_f = max(ratio_f, r) 
                if ratio_f < th1:
                    totalfactory.append(val) 
                    #print(val)
        for val in temp_n:
            ratio_n = 0
            if init_n:
                totalname.append(val)
                #print(val)
                init_n = 0
            else:
                for j in totalname:
                    r = compare_str(j, val)
                    ratio_n = max(ratio_n, r) 
                if ratio_f < th2:
                    totalname.append(val) 
                    #print(val)
    totalfactory.sort()
    totalname.sort()
    return (totalfactory, totalname)       
        

# 帮助run Maldives5.2.0.py --help
if __name__ == '__main__':
    
    total = 4
    th1 = 0.98
    th2 = 0.98
    totalfactory, totalname = allfactory(total, th1, th2)
         