# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

马尔代夫V3.0

实现了对于指定网页集合的批量信息抓取

"""

import sys
import getopt
import csv, requests
from bs4 import BeautifulSoup

# 全局变量定义
g_dict = {}

# 获取所有字典并生成表头
def get_all_dict():
    for url in urls:
        # 获取网页
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        
        # 得到表格并声明临时存储变量
        table_content = soup.select(".techspecs td")
        content = {}
        # 得到字典
        index = 1
        pre = ''
        for i in table_content:
            if index % 2 == 0:
                content[pre] = i.get_text()
            pre = i.get_text()
            index += 1
            
        # 更新全局字典
        global g_dict
        for key, value in content.items():
            g_dict[key] = value
        
        # 存储表头
        with open(file_table, 'w', newline='') as f:
            writer = csv.writer(f)
            row = []
            for key in sorted(g_dict.keys()):
                row.append(key)
            writer.writerow(row)
            f.close()
            
        # 存储特性
        with open(file_feature, 'w', newline='') as f:
            f.close()  
        

# 存储新的表
def save_csv(url):
    # 获取网页
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    
    # 得到表格并声明临时存储变量
    table_content = soup.select(".techspecs td")
    content = {}
    # 得到字典
    index = 1
    pre = ''
    for i in table_content:
        if index % 2 == 0:
            content[pre] = i.get_text()
        pre = i.get_text()
        index += 1
    
    # 初始化并更新全局字典
    global g_dict
    for key in g_dict.keys():
        g_dict[key] = ''
    g_dict.update(content) 
    
     # 存储表
    with open(file_table, 'a', newline='') as f:
        writer = csv.writer(f)
        row = []
        for key in sorted(g_dict.keys()):
            row.append(g_dict[key])
        writer.writerow(row)
        f.close()
    
    # 得到特性
    detail = []
    for i in soup.select("#lt_col > ul li"):
        detail.append(i.get_text())

    # 存储特性
    with open(file_feature, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(detail)
        f.close()

# 帮助run Maldives3.0.py --help
# 测试运行run Maldives3.0.py --table 'xx.csv' --feature 'yy.csv'
# 测试运行run Maldives3.0.py -t 'xx.csv' -f 'yy.csv'
if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'ht:f:w:', [ 'help', 'table=', 'feature=', 'web='  ])

    file_table = "csv_table.csv"
    file_feature = "csv_feature.csv"
    file_web = "csv_web.csv"
    
    for key, value in opts:

        if key in ['-h', '--help']:
            print('马尔代夫V3.0')
            print('参数定义：')
            print('-h, --help\t显示帮助')
            print('-t, --table\t表存储CSV文件')
            print('-f, --feature\t特性存储CSV文件')
            print('-wf, --web\t来源网址CSV文件')
            sys.exit(0)
        if key in ['-t', '--table']:
            file_table = value
        if key in ['-f', '--feature']:
            file_feature = value
        if key in ['-w', '--web']:
            file_web = value

    print('马尔代夫V3.0\tTable stored in:', file_table, '\tFeature stored in:', file_feature, '\tWeb from:', file_web) 
    
   # 得到所有urls
    urls = []
    with open("csv_web.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            urls.append(row['web'])
    
    # 得到表头
    get_all_dict()
    
    # 保存数据
    for url in urls:
        save_csv(url)
    
    

