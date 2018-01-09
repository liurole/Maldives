# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 21:49:03 2018

@author: Se

提取主题时获取网页链接
"""

import sys
import re
import getopt
import csv, requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    
    url = 'https://www.wolfspeed.com/power/products/sic-mosfets/table'
    
    
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    
    index = 0
    for link  in soup.find_all(name='a',attrs={"href":re.compile(r'^https://www.wolfspeed.com/media/downloads/')}):
        index += 1
        print(link.get('href') )  
    
    print(index)
    