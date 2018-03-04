# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

马尔代夫V3.3

实现了批量pdf下载

"""
import xlrd 
import sys
import getopt
import urllib

def getFile(url, index):
    file_name = url.split('/')[-1]
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
    req = urllib.request.Request(url, headers=headers) 
    data = urllib.request.urlopen(req).read()  
    f = open('./pdf/' + file_name, 'wb') 
    f.write(data)  
    f.close()
    str_out = "Sucessful to download" + " " + file_name + "    " + str(index)
    print (str_out)

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

# 帮助run Maldives3.0.py --help
if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'h', [ 'help' ])
    
    for key, value in opts:

        if key in ['-h', '--help']:
            print('马尔代夫V5.6.4')
            print('用于批量保存pdf')
            sys.exit(0)
    
    tables = excel_table_byindex('./data/detail.xlsx', 0, 3) 
      
    # 得到所有urls
    urls = []
    
    for row in tables: 
        urls.append(row['ref'])    
    
    done = []
    index = 1
    # 保存数据
    for url in urls:
        if url != '' and not(url in done) and index > 0:
            try:
                getFile(url, index)
            except:
                pass
            done.append(url)
            index += 1
            
    print('All done!')