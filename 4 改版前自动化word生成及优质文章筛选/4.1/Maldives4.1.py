# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

马尔代夫V4.1

实现了优质产品的查找（信息齐全）

"""

import sys
import getopt
import csv

# 帮助run Maldives4.1.py --help
if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hi:', [ 'help', 'index=' ])
    
    index = 1
    r_num = []
    r_val = []
    
    err = []
    
    # 入口函数
    for key, value in opts:
        if key in ['-h', '--help']:
            print('马尔代夫V4.1')
            print('参数定义：')
            print('-h, --help\t显示帮助')
            print('-i, --index\t序号')
            sys.exit(0)
        if key in ['-i', '--index']:
            index = value
    print('马尔代夫V4.1 function with num: ', index ) 
    
    
    num = []
    larest = []
    index = 0
    # 查找index
    with open("detail.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            index += 1
            temp = 0
            for key, value in row.items():
                if value == '':
                    pass
                else:
                    temp += 1
            #print(temp)  
            num.append(temp)
            if temp == 19:
                larest.append(index)
                print(index)
            
    print('共：', len(larest))
            