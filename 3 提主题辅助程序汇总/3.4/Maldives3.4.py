# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

拟定题目

"""

import sys
import getopt
import csv
import codecs

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'h', [ 'help'])
    
    file_detail = 'detail.csv'
    file_title = 'title.csv'
    file_dir = './3.4/'
    
    for key, value in opts:

        if key in ['-h', '--help']:
            print('马尔代夫V4.3.2')
            print('参数定义：')
            print('-h, --help\t显示帮助')
            sys.exit(0)

    print('马尔代夫3.4') 
    
    file_in = file_dir + file_detail
    file_out = file_dir + file_title
    
    print('From:\t', file_in)
    print('To:\t', file_out)
    
    # 得到所有细节
    i_f = []
    i_r = []
    v_r = []
    package = []
    category = []
    
    my_title = []
   
    with codecs.open(file_in, "r", 'utf_8_sig') as f:
        reader = csv.reader(f)
        for row in reader :
            i_f.append(row[2])
            i_r.append(row[6])
            v_r.append(row[7])
            package.append(row[8])
            category.append(row[11])
        f.close()   
    
    for i in range(0, len(i_f)):
        title = '最大整流电流' + i_f[i] + 'A，' + '反向工作电压' + v_r[i] + 'V，一款' + package[i] + '封装的'
        if category[i] == '1':
            title += '肖特基二极管'
        elif category[i] == '2':
            title += '一般整流二极管'
        elif category[i] == '3':
            title += '桥式整流二极管'
        elif category[i] == '4':
            title += '快恢复二极管'
        my_title.append(title)
    
    # 存储特性
    with codecs.open(file_out,"w",'utf_8_sig') as f:
        writer = csv.writer(f)
        for title in my_title:
            row = []
            row.append(title)
            writer.writerow(row)
        f.close()     
    
    


