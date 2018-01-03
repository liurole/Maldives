# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

马尔代夫V5.2.0

实现了同类产品型号的合并

"""

import sys
import getopt
import csv
import codecs
import difflib

def compare_str(first, second):
    seq = difflib.SequenceMatcher(lambda x: x in '-', first, second)  
    ratio = seq.ratio()
    return ratio    

# 帮助run Maldives5.2.0.py --help
if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hi:', [ 'help' ])
    
    # 入口函数
    for key, value in opts:
        if key in ['-h', '--help']:
            print('马尔代夫V5.2.0')
            print('参数定义：')
            print('-h, --help\t实现了同类产品型号的合并')
            sys.exit(0)    
    
    types =[]
    # 查找index
    with open("detail.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            temp = row['型号']
            temp_list = temp.split('-')
            temp = ''
            for i in range(len(temp_list) - 1):
                if i == 0:
                    temp += temp_list[i]
                else:
                    temp += '-' + temp_list[i]
            types.append(temp)
            
    type_id = 0
    type_store = []
    for i, val in enumerate(types):
        if i == 0:
            type_store.append(type_id)
        else:
            ratio = compare_str(types[i - 1], val)
            if ratio < 0.95:
                type_id += 1
            type_store.append(type_id)
                
    with codecs.open('型号归类.csv',"w",'utf_8_sig') as f:
        writer_a = csv.writer(f)
        for i, val in enumerate(types):
            row = []
            row.append(val)
            row.append(type_store[i])
            writer_a.writerow(row)
        f.close()         