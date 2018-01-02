# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

马尔代夫V3.3

实现了批量pdf下载

"""

import sys
import getopt
import csv
import urllib

def getFile(url):
    file_name = url.split('/')[-1]
    urllib.request.urlretrieve(url, file_dir + 'pdf/' + file_name)
    print ("Sucessful to download" + " " + file_name)


# 帮助run Maldives3.0.py --help
if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'h', [ 'help' ])

    file_web = "csv_web.csv"
    file_dir = './v3.3/'
    
    for key, value in opts:

        if key in ['-h', '--help']:
            print('马尔代夫V3.3')
            print('用于批量保存pdf')
            sys.exit(0)

    print('马尔代夫V3.3\tStored in:', file_dir, '\tFrom:', file_web) 
    
   # 得到所有urls
    urls = []
    with open(file_dir + file_web) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            urls.append(row['web'])
            
    
    # 保存数据
    for url in urls:
        if url != '':
            try:
                urllib.request.urlopen(url)
                getFile(url)
            except:
                pass
            
    print('All done!')