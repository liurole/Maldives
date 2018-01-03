# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

马尔代夫V5.3.4

实现了应用特性遗漏商品的查找

"""

import sys
import getopt
import csv

# 帮助run Maldives5.3.4.py --help
if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hi:', [ 'help', 'index=' ])
    
    r_num = []
    r_val = []
    
    err = []
    
    # 入口函数
    for key, value in opts:
        if key in ['-h', '--help']:
            print('马尔代夫V5.3.4')
            print('参数定义：')
            print('-h, --help\t显示帮助')
            sys.exit(0)
    
    num = []
    index = 0
    # 查找index
    with open("detail.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            index += 1
            temp = 0
            for key, value in row.items():
                if key != '应用' and key != '特性1' and key != '特性2':
                    if value == '':
                        pass
                    else:
                        temp += 1
            if temp == 16:
                num.append(index)
                print(index)
        csvfile.close()
    print('共：', len(num))
    
    index = 0
    empty = []
    # 查找index
    with open("detail.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            index += 1
            if index in num:
                for key, value in row.items():
                    if key != '应用' or key != '特性1' or key != '特性2':
                        if value == '':
                            empty.append(index)
                            break
        csvfile.close()
    for i, val in enumerate(empty):
        print(val)
    print('共：', len(empty))    
    
            