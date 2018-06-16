# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:44:45 2018

@author: Se

下载chromedrive驱动 
使用Selenium需要选择一个调用的浏览器并下载好对应的驱动，本文使用chrome浏览器，当然也可以用FireFox等
http://www.seleniumhq.org/download/ 找到Google Chrome Driver链接
对应驱动放在python目录下面的scripts目录中，例如C:\ProgramData\Anaconda3\envs\python35\Scripts

实现了利用本地cookie文件的登录
"""
import re
import requests
import json
import numpy as np
import pandas as pd
import time

def get_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        return None

def get_info(temp):
    data = {}
    str_temp = temp
    if '(Equipment)' in str_temp:
        str_temp = str_temp[:-12]
    if ' ' in str_temp:
        str_temp = re.sub(' ', '%20', str_temp)
    if '(' in str_temp:
        str_temp = re.sub('(', '%28', str_temp)
    if ')' in str_temp:
        str_temp = re.sub(')', '%29', str_temp)
    if '™' in str_temp:
        str_temp = re.sub('™', '%E2%84%A2', str_temp)
    if '|' in str_temp:
        str_temp = re.sub('|', '%7C', str_temp)
    url = 'https://steamcommunity.com/market/priceoverview/?country=CN&currency=23&appid=570&market_hash_name=' + str_temp
    html = get_html(url)
    if html is None:
        data['市场可交易'] = 0
        data['平均价格'] = 0
        data['最低价格'] = 0
    else:
        content = json.loads(html)
        data['市场可交易'] = 1
        if 'median_price' in content.keys():
            temp_content = content['median_price']
            if '¥ ' in temp_content:
                temp_content = re.sub('¥ ', '', temp_content)
            data['平均价格'] = temp_content
        else:
            data['平均价格'] = 666
        if 'lowest_price' in content.keys():
            temp_content = content['lowest_price']
            if '¥ ' in temp_content:
                temp_content = re.sub('¥ ', '', temp_content)
            data['最低价格'] = temp_content
        else:
            data['最低价格'] = 666
           
    return data

if __name__ == '__main__':
    
    time_start = time.time()
    # 读取Excel
    file = '刀塔所有英雄饰品缺少统计.xlsx'
    result_web = pd.read_excel(file)
    
    # 创建一个空的 DataFrame  
    df = pd.DataFrame(columns=['市场可交易', '平均价格', '最低价格'])  
    num = 1
    
    for index in result_web.index:
        if index > 1365 and index < 6530:
            time.sleep(3)
            if np.asscalar(result_web['拥有'][index]) == 0:
                temp = result_web['物品名称'][index]
                data = get_info(temp)
                df.loc[index, '市场可交易'] = data['市场可交易']
                df.loc[index, '平均价格'] = data['平均价格']
                df.loc[index, '最低价格'] = data['最低价格']
                time_end = time.time()
                print(temp + '  ' + str(num) + '/' + str(len(result_web)) + '  ' + str(data['最低价格']) + '  ' + str(time_end - time_start))
            else:
                df.loc[index, '市场可交易'] = -1
                df.loc[index, '平均价格'] = -1
                df.loc[index, '最低价格'] = -1
        num += 1
        
    result = pd.concat([result_web, df], axis=1)
    result.to_excel("刀塔缺少英雄饰品价格统计.xlsx", index=False)     # write data to excel 
    
    
#    curAbbrev = {
#    'USD' : 1,
#    'GBP' : 2,
#    'EUR' : 3,
#    'CHF' : 4,
#    'RUB' : 5,
#    'KRW' : 16,
#    'CAD' : 20,
#    'RMB' : 23
#    }
    
#kk= df[0:1300]
#
#kk.to_csv("data1.csv")