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
def get_all(url):
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
    
    # 存储表
    with codecs.open(file_dir + file_feature,"a",'utf_8_sig') as f:
        writer_a = csv.writer(f)
        writer_a.writerow(temp)
        f.close()           
    

# 得到详情与pdf子链接
def get_urls(url):

    html = requests.get(url)
    html.encoding ='utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    
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
                pdf_urls.append('http://www.shindengen.co.jp' + temp)
            

# 得到参考页面所有特性
def get_details(url):

    html = requests.get(url)
    html.encoding ='utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    
    # 得到表格并声明临时存储变量
    table_content = soup.select("td")
    
#    for i in table_content:
#        print(i.get_text())
    
    # 存储表
    with codecs.open(file_dir + file_detail,"w",'utf_8_sig') as f:
        writer = csv.writer(f)
        row = []
        for i, val in enumerate(table_content):
            if i % num == 0:
                string = str(val.get_text())
                if string.startswith('new'):
                    string = string.split('!')
                    row.append(string[1])           # 保存型号名字，去除new
                    names.append(string[1])         # 保存型号名字，去除new
                else:
                    row.append(string)
                    names.append(string)                    
            elif i % num > 2 and i % num < num - 1:
                row.append(val.get_text())
            elif i % num == num - 1:
                writer.writerow(row)                # 最后一列不保存
                row = []                        
        f.close()

# 帮助run Maldives3.2.py --help
# 帮助run Maldives3.2.py -c 01 -s 01 -n 14
# 帮助run Maldives3.2.py -c 01 -s 03 -n 14
# 帮助run Maldives3.2.py -c 01 -s 04 -n 15
# 帮助run Maldives3.2.py -c 01 -s 05 -n 15
# 帮助run Maldives3.2.py -c 03 -s 01 -n 13
# 帮助run Maldives3.2.py -c 03 -s 02 -n 13
# 帮助run Maldives3.2.py -c 04 -s 03 -n 9
# 帮助run Maldives3.2.py -c 04 -s 01 -n 10
# 帮助run Maldives3.2.py -c 05 -s 02 -n 10
# 帮助run Maldives3.2.py -c 06 -s 01 -n 10
# 帮助run Maldives3.2.py -c 06 -s 02 -n 10
# 帮助run Maldives3.2.py -c 07 -s 04 -n 11
# 帮助run Maldives3.2.py -c 07 -s 03 -n 11
# 帮助run Maldives3.2.py -c 07 -s 01 -n 10
if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hc:s:n:', [ 'help', 'category=', 'sub_id=' ])

    # 输入变量
    category = '01'
    sub_id = '04'
    num = 15
    web_p = 'http://www.shindengen.co.jp/product_e/semi/search_NEW.php?'
    
    # 输出文件
    file_detail = 'detail.csv'
    file_web = 'web.csv'
    file_dir = './v3.2/'
    
    # 储存变量
    names = []
    sub_urls = []
    pdf_urls = []
    
    for key, value in opts:
        if key in ['-h', '--help']:
            print('马尔代夫V3.2')
            print('参数定义：')
            print('-h, --help\t显示帮助')
            print('-c, --category\t类别序号')
            print('-s, --sub_id\t子类别序号')
            print('-n, --num\t列数')
            sys.exit(0)
        if key in ['-c', '--category']:
            category = value
        if key in ['-s', '--sub_id']:
            sub_id = value
        if key in ['-n', '--num']:
            num = int(value)

    # 信息输出
    print('马尔代夫V3.2\tCategory ID:', category, '\tSub ID:', sub_id) 
    web_a = web_p + 'category_id=' + category + '&sub_id=' + sub_id
    print(web_a)
    
    # 获取该汇总页面的所有信息
    get_details(web_a)

    # 得到详情与pdf子链接    
    get_urls(web_a)
    
    # 存储详情与pdf子链接 
    with codecs.open(file_dir + file_web,"w",'utf_8_sig') as f:
        writer = csv.writer(f)
        for i in range(0, len(names)):
            temp = []
            temp.append(names[i])
            temp.append(sub_urls[i])
            temp.append(pdf_urls[i])
            writer.writerow(temp)
        f.close()    
    
#    index = 0
#    for url in sub_urls:
#        index += 1
#        print('Running:\t' + str(index))
#        get_all(url)


