# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 22:03:08 2018

@author: Se

下载chromedrive驱动 
使用Selenium需要选择一个调用的浏览器并下载好对应的驱动，本文使用chrome浏览器，当然也可以用FireFox等
http://www.seleniumhq.org/download/ 找到Google Chrome Driver链接
对应驱动放在python目录下面的scripts目录中，例如C:\ProgramData\Anaconda3\envs\python35\Scripts
"""
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlencode

# 利用request，导入cookies，header进行关键词网页搜索，选择第二栏
def check_repeated(keyword, tab):
    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'X-Requested-With': 'XMLHttpRequest'
    }
    cookies = {
    'at': 'eyJ1c2VyX2lkIjoiMTYzMTQ0MCIsImlzcyI6ImNvaW5jb2xhLmNvbSIsImV4cCI6MTUxOTQ1MjQ1MiwiaWF0IjoxNTE4ODQ3NjUyLCJkZXZpY2UiOiJXRUIiLCJqdGkiOiJkNTFkMjdjYS1kN2QwLTQzY2ItOTUyMC1iYzQxZTc3OGE4OGYifQ',
    'name': 'liurole',
    'hpp': 'true',
    'ccy': 'OSC',
    'ctc': 'ETH_BTC'
    }
    data = {
        'tab': str(tab),
    }
    params = urlencode(data)
    base = 'https://www.sekorm.com/Web/Search/keyword/'
    url = base + keyword + '?' + params
    try:
        response = requests.get(url, cookies = cookies, headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        return None

# 获取所有搜索结果链接
def get_all_urls(html):
    names = []
    urls = []
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('#multiple-search_0 a')
    if len(result) == 0:
        return names, urls
    else:
        for i in result:
            temp = i.get('href')
            urls.append(temp)
            temp = i.get_text()
            names.append(temp)
        return names, urls

# 搜索所有子链接，在子页面进行查找，发现是否包括此关键词
def search_all_urls(urls, keyword, length = 20):
    length = min(length, len(urls))
    for i in range(length):
        html = urls[i]
        response = requests.get(html)
        soup = BeautifulSoup(response.text, 'lxml')
        result = soup.select('.cd-content p')
        for j in result:
            temp = result = re.sub(r'[^\x00-\x7F]+', '', j.get_text())
            if keyword in temp:
                return True
    return False

if __name__ == '__main__':
    
    keyword = 'D200LC40B'
    tab = 1

    html = check_repeated(keyword, tab)
    names, urls = get_all_urls(html)
    repeated = search_all_urls(urls, keyword)
    
    print(repeated)
    