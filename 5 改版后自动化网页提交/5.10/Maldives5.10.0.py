# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:13:31 2018

@author: Se

马尔代夫V5.10.0

实现了型号还有超链接的输出
"""

import xlrd

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

if __name__ == '__main__':
    
    tables = excel_table_byindex('京瓷型号表.xlsx', 0, 2) 
    
    types = ''
    refs = ''
    init = True
    
    for i in tables:
        if init:
            types += i['型号']
            refs += i['网址']
            init = False
        else:
            types += '，' + i['型号']
            refs += '，' + i['网址']           

    refs += '（部分网络需要VPN才能访问）'
    print(types)
    print('')
    print(refs)
