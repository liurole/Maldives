# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

为新电元而生

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

    file_search = './data/detail.xlsx'
    file_pass = './../新电元剩余产品.xlsx'
    
    tables_search = excel_table_byindex(file_search, 0, 3)  
    tables_pass = excel_table_byindex(file_pass, 0, 4)  
    
    list_search = []
    list_pass = []
    
    for row in tables_search:
        list_search.append(row['型号'])
    
    for row in tables_pass:
        list_pass.append(row['型号'])    
    
    for i in list_search:
        if i in list_pass:
            print('1')
        else:
            print('0')
        
