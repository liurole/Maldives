# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:51:34 2018

@author: Se
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

    # 查找详情
    data = open_excel('京瓷撰写情况.xlsx')
    table = data.sheets()[7]
    nrows = table.nrows #行数   
    colnames = table.row_values(0)      #某一行数据 
    
    
    num = []
    for i in range(len(colnames)):
        num.append(0)
        
    for rownum in range(1, 133):  
        row = table.row_values(rownum)#以列表格式输出  
        for i in range(len(colnames)):  
            if row[i] != '':
                num[i] += 1
    
    for i in range(len(colnames)):
        if num[i] != 132:
            print(i, num[i])
           
