# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 11:38:47 2017

@author: liurole

实现了字符串相似程度的比较

"""

import sys
import getopt
import difflib

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hf:s:', [ 'help', 'first=', 'second=' ])
    
    # 入口函数
    for key, value in opts:
        if key in ['-h', '--help']:
            print('参数定义：')
            print('-h, --help\t使用帮助')
            print('-f, --first\t第一个字符串')
            print('-s, --second\t第二个字符串')
            sys.exit(0) 
        if key in ['-f', '--first']:
            first = value
        if key in ['-s', '--second']:
            second = value
            
    seq = difflib.SequenceMatcher(lambda x: x in '-', first, second)  
    ratio = seq.ratio()
    print(ratio)
      