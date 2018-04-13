# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 22:03:08 2018

@author: Se

start, end格式为2014, 8, 3这样
只需要每次更改datelist中的两个起止日期

"""

import datetime
import urllib

def datelist(start, end):
    start_date = datetime.date(*start)
    end_date = datetime.date(*end)

    result = []
    curr_date = start_date
    while curr_date != end_date:
        result.append("%04d%02d%02d" % (curr_date.year, curr_date.month, curr_date.day))
        curr_date += datetime.timedelta(1)
    result.append("%04d%02d%02d" % (curr_date.year, curr_date.month, curr_date.day))
    return result



if __name__ == '__main__':
    
    data = datelist((2018, 4, 1), (2018, 4, 3))
    urls = []
    for i in data:
        url = 'http://lcache.qingting.fm/cache/' + i + '/20083/20083_' + i + '_130000_140000_24_0.aac'
        urls.append(url)
        temp = i + '璐姐侃房' + i + '.aac'
        try:
            urllib.request.urlretrieve(url, temp)
            print('日期---' + i + '---下载成功')
        except:  
            print('日期---' + i + '---下载失败')
            print('\t' + temp)
        