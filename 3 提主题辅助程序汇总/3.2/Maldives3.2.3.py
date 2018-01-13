# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

为新电元而生

"""

import sys
import re
import getopt
import csv, requests
import urllib
import chardet 
import codecs
from bs4 import BeautifulSoup
import xlrd 

"""
解决乱码问题的途径
第一种二进制保存：
import pickle
# 写文件
output = open('data.pkl', 'wb')
pickle.dump(content, output)
output.close()
# 读文件
pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
pkl_file.close()
第二种正则化已知乱码字符
selector函数的实现
"""

def detect(url):
    fp = urllib.request.urlopen(url)
    blog = fp.read()
    codedetect = chardet.detect(blog)['encoding']
    print(codedetect)
    fp.close()

def selector(t):
    bChange = 0
    if 'ã' in t:
        t = re.sub('[^0-9\-]','',t)
        if len(t) == 6:
            t = t[:3] + '-' + t[3:] #表示温度，故中间加一个过渡符
            bChange = 1
    return t, bChange


# 得到所有细节
def get_all(url, num):
    html = requests.get(url)
    html.encoding ='utf-8'
    soup = BeautifulSoup(html.text, 'lxml')    
    
    # 得到表格并声明临时存储变量
    table_content = soup.select('td')
    content = {}
    # 得到字典
    index = 1
    pre = ''
    for i in table_content:
        if index % 2 == 0:
            content[pre] = i.get_text()
        pre = i.get_text()
        index += 1
    
    t1 = content['Tj (℃)']
    t2 = content['Tstg (℃)']

    t1, bChange1 = selector(t1)
    t2, bChange2 = selector(t2)
    content['Tj (℃)'] = t1
    content['Tstg (℃)'] = t2
    
    # 存储表
    """
    Contidion Ta (℃)
    Contidion Tc (℃)
    IF (A)
    IFSM (A) 
    Tj (℃)
    Tstg (℃)
    VRRM (V)
    """
    
    with codecs.open(file_dir + file_table,"a",'utf_8_sig') as f:
        writer_a = csv.writer(f)
        row = []
        for key in sorted(content.keys()):
            row.append(content[key])
            # print(key)
        writer_a.writerow(row)
        f.close()    
    
    # 得到特性并声明临时存储变量
    temp = []
    table_content = soup.select('#semi_center ul')
    temp_content = table_content[0].get_text()
    temp.append(temp_content)
    temp.append(num)
    
    # 存储表
    with codecs.open(file_dir + file_feature,"a",'utf_8_sig') as f:
        writer_a = csv.writer(f)
        writer_a.writerow(temp)
        f.close()           

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

    file_web = 'search_feature.xlsx'
    file_out = 'cut_feature.csv'
    file_dir = './v3.2/'
    
    # 得到所有urls
    tables = excel_table_byindex(file = file_dir + file_web)  
    

    for row in tables:
        url = row['内容']
        url = url[:-1]
        temp = url.strip()
        print(temp)
#       url = url.split('•')
#       print(url[1])


    


        
