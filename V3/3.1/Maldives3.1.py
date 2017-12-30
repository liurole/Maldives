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
from bs4 import BeautifulSoup


"""
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
"""

def selector(t):
    bChange = 0
    if 'ã' in t:
        t = re.sub('[^0-9\-]','',t)
        if len(t) == 6:
            t = t[:3] + '-' + t[3:]
            bChange = 1
    return t, bChange


# 得到所有细节
def get_all(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')    
    
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
    with open(file_dir + file_table, 'a', newline='') as f:
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
    temp_content = re.sub('[^a-zA-Z0-9\=\s]','',temp_content)
    temp.append(temp_content)
    
    # 存储表
    with open(file_dir + file_feature, 'a', newline='') as ft:
        writer_a = csv.writer(ft)
        writer_a.writerow(temp)
        ft.close()           
    
    

# 得到所有子链接
def get_urls(url):

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    
    # 得到表格并声明临时存储变量
    table_content = soup.find_all('a')

    for i in table_content:
        temp = str(i.get('href'))
        if temp.startswith('list_detail_NEW.php'):
            sub_urls.append('http://www.shindengen.co.jp/product_e/semi/' + temp)
        elif temp.startswith('/product/semi'):
            if temp.endswith('Under development'):
                pdf_urls.append('')
            else:
                pdf_urls.append('http://www.shindengen.co.jp/' + temp)
            

# 得到所有特性
def get_details(url):

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    
    # 得到表格并声明临时存储变量
    table_content = soup.select("td")
    
#    for i in table_content:
#        print(i.get_text())
    
    # 存储表
    with open(file_dir + file_detail, 'w', newline='') as f:
        writer = csv.writer(f)
        row = []
        for i, val in enumerate(table_content):
            
            if i % 15 == 0:
                string = str(val.get_text())
                if string.startswith('new'):
                    string = string.split('!')
                    row.append(string[1])
                    names.append(string[1])
                else:
                    row.append(string)
                    names.append(string)                    
            elif i % 15 > 2 and i % 15 < 14:
                row.append(val.get_text())
            elif i % 15 == 14:
                writer.writerow(row)
                row = []
        f.close()

# 帮助run Maldives3.1.py --help
# 帮助run Maldives3.1.py -c 01 -s 04
if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hc:s:', [ 'help', 'category=', 'sub_id=' ])

    category = '01'
    sub_id = '04'
    web_p = 'http://www.shindengen.co.jp/product_e/semi/search_NEW.php?'
    
    file_detail = 'detail.csv'
    file_web = 'web.csv'
    file_table = 'table.csv'
    file_feature = 'feature.csv'
    file_dir = './v3.1/'
    
    names = []
    sub_urls = []
    pdf_urls = []
    
    for key, value in opts:

        if key in ['-h', '--help']:
            print('马尔代夫V3.0')
            print('参数定义：')
            print('-h, --help\t显示帮助')
            print('-c, --category\t类别序号')
            print('-s, --sub_id\t子类别序号')
            sys.exit(0)
        if key in ['-c', '--category']:
            category = value
        if key in ['-s', '--sub_id']:
            sub_id = value

    print('马尔代夫V3.1\tCategory ID:', category, '\tSub ID:', sub_id) 
    
    web_a = web_p + 'category_id=' + category + '&sub_id=' + sub_id
    print(web_a)
    
    get_details(web_a)
    
    
    get_urls(web_a)
    
    # 存储特性
    with open(file_dir + file_web, 'w', newline='') as f:
        writer = csv.writer(f)
        for i in range(0, len(names)):
            temp = []
            temp.append(names[i])
            temp.append(sub_urls[i])
            temp.append(pdf_urls[i])
            writer.writerow(temp)
        
        f.close()    
    
    for url in sub_urls:
        get_all(url)


