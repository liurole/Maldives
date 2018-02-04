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

def getseparate(id):
    totalfactory = []
    totalname = []    
    tables = excel_table_byindex('总结.xlsx', 0, id)
    for i in range(len(tables)):
        temp_f = tables[i]['厂牌']
        temp_n = tables[i]['姓名']
        if '翻译' in temp_n:
            temp_n = temp_n[:-4]
        temp_f = re.sub('[^a-zA-Z\s]', '', temp_f).lower()
        temp_f = temp_f.rstrip()
        if temp_f == '':
            continue 
        totalfactory.append(temp_f)
        totalname.append(temp_n)
            
    data = [(factory, name) for factory, name in zip(totalfactory, totalname)] #先转化成元组
    data.sort() #按照分数排序
    totalfactory = [factory for factory, name in data] #将排好序的分数姓名的元组分开
    totalname = [name for factory, name in data]            

    return (totalfactory, totalname) 

def getinfo(total):
    totalfactory = []
    totalname = []
    for id in range(total):
        tables = excel_table_byindex('总结.xlsx', 0, id)
        for i in range(len(tables)):
            temp_f = tables[i]['厂牌']
            temp_n = tables[i]['姓名']
            if '翻译' in temp_n:
                temp_n = temp_n[:-4]
            temp_f = re.sub('[^a-zA-Z\s]', '', temp_f).lower()
            temp_f = temp_f.rstrip()
            if temp_f == '':
                continue 
            totalfactory.append(temp_f)
            totalname.append(temp_n)
            
    data = [(factory, name) for factory, name in zip(totalfactory, totalname)] #先转化成元组
    data.sort() #按照分数排序
    totalfactory = [factory for factory, name in data] #将排好序的分数姓名的元组分开
    totalname = [name for factory, name in data]            

    return (totalfactory, totalname)       

# 帮助run Maldives5.2.0.py --help
if __name__ == '__main__':
    
    total = 4
    totalfactory, totalname = getinfo(total)
    factory = set(totalfactory)
    name = set(totalname)
    
#    # 统计总的厂牌分布情况，数据库中所有厂牌每个被写了多少篇
#    factory_detail = {}
#    for item in factory:
#        factory_detail[item] = totalfactory.count(item)    
    
    # 统计每个月各个厂牌被写了多少篇
    list_factory_num_ = []
    for id in range(total):
        tempfactory, tempname = getseparate(id)
        temp_detail = {}
        for item in factory:
            temp_n = tempfactory.count(item) 
            if temp_n != 0:
                temp_detail[item] = temp_n   
        list_factory_num_.append(temp_detail)          

    # 统计每个月各个厂牌每个人都写了多少篇
    list_factory_detail = []
    name_list = list(set(totalname))
    name_list.sort(key = totalname.index) 
    for id in range(total):
        temp_factory = {}
        temp_detail = list_factory_num_[id]
        tempfactory, tempname = getseparate(id)
        for key,value in temp_detail.items():
            temp_name = {}
            for i in name_list:
                temp_name[i] = 0
            for i, val in enumerate(tempfactory):
                if val == key:
                    temp_name[tempname[i]] += 1
            temp_factory[key] = temp_name
        list_factory_detail.append(temp_factory)
        
    # 统计每个月各个人写了多少篇
    list_name_num = []
    for id in range(total):
        tempfactory, tempname = getseparate(id)
        temp_detail = {}
        for item in name:
            temp_n = tempname.count(item) 
            if temp_n != 0:
                temp_detail[item] = temp_n   
        list_name_num.append(temp_detail)          

    # 统计每个月各个厂牌每个人都写了多少篇
    list_name_detail = []
    factory_list = list(set(totalfactory))
    factory_list.sort(key = totalfactory.index) 
    for id in range(total):
        temp_name = {}
        temp_detail = list_name_num[id]
        tempfactory, tempname = getseparate(id)
        for key,value in temp_detail.items():
            temp_factory = {}
            for i in factory_list:
                temp_factory[i] = 0
            for i, val in enumerate(tempname):
                if val == key:
                    temp_factory[tempfactory[i]] += 1
            temp_name[key] = temp_factory
        list_name_detail.append(temp_name)
    
    # 各个类型统计
    list_other_num = []
    for id in range(total):
        temp_num = {}
        temp_num['应用'] = 0
        temp_num['选型'] = 0
        temp_num['新技术'] = 0
        tables = excel_table_byindex('总结.xlsx', 0, id)
        for i in range(len(tables)):
            temp = tables[i]['题目']
            if '【应用】' in temp:
                temp_num['应用'] += 1
            elif '【选型】' in temp:
                temp_num['选型'] += 1
            elif '【新技术】' in temp:
                temp_num['新技术'] += 1        
        list_other_num.append(temp_num)
                 
    
    
    
         