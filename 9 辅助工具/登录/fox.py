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
import json
from json.decoder import JSONDecodeError

def get_page_index(id):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTYzMTQ0MCIsImlzcyI6ImNvaW5jb2xhLmNvbSIsImV4cCI6MTUxOTQ2NjYxMCwiaWF0IjoxNTE4ODYxODEwLCJkZXZpY2UiOiJXRUIiLCJqdGkiOiIyNjE0NzY4NC0yNjU5LTQxOTEtOGI5YS1jMTQ5MDU5MzIzZTkifQ.Ac6Dm07kYOsMzOl87kjPMLPLVyAI9e7D1u2F8Z4N9PY',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
    }
    cookies = {
    'at': 'eyJ1c2VyX2lkIjoiMTYzMTQ0MCIsImlzcyI6ImNvaW5jb2xhLmNvbSIsImV4cCI6MTUxOTQ1MjQ1MiwiaWF0IjoxNTE4ODQ3NjUyLCJkZXZpY2UiOiJXRUIiLCJqdGkiOiJkNTFkMjdjYS1kN2QwLTQzY2ItOTUyMC1iYzQxZTc3OGE4OGYifQ',
    'name': 'liurole',
    'hpp': 'true',
    'ccy': 'OSC',
    'ctc': 'ETH_BTC'
    }
    url = 'https://www.51lkh.com/game/fox/' + str(id)
    try:
        response = requests.get(url, cookies = cookies, headers = headers)
        if response.status_code == 200:
            return response
        return None

    except ConnectionError:
        print('Error occurred')
        return None

def parse_page_index(text):
    try:
        data = json.loads(text)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('birth_dig')
    except JSONDecodeError:
        pass

if __name__ == '__main__':
    
#    # 测试1
#    s = requests.Session()
#    headers = {
#    'Accept': 'application/json, text/plain, */*',
#    'Accept-Encoding': 'gzip, deflate, br',
#    'Accept-Language': 'zh-CN,zh;q=0.8',
#    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTYzMTQ0MCIsImlzcyI6ImNvaW5jb2xhLmNvbSIsImV4cCI6MTUxOTQ2NjYxMCwiaWF0IjoxNTE4ODYxODEwLCJkZXZpY2UiOiJXRUIiLCJqdGkiOiIyNjE0NzY4NC0yNjU5LTQxOTEtOGI5YS1jMTQ5MDU5MzIzZTkifQ.Ac6Dm07kYOsMzOl87kjPMLPLVyAI9e7D1u2F8Z4N9PY',
#    'Connection': 'keep-alive',
#    'Content-Length': '0',
#    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
#    }
#    cookies = {
#    'at': 'eyJ1c2VyX2lkIjoiMTYzMTQ0MCIsImlzcyI6ImNvaW5jb2xhLmNvbSIsImV4cCI6MTUxOTQ1MjQ1MiwiaWF0IjoxNTE4ODQ3NjUyLCJkZXZpY2UiOiJXRUIiLCJqdGkiOiJkNTFkMjdjYS1kN2QwLTQzY2ItOTUyMC1iYzQxZTc3OGE4OGYifQ',
#    'name': 'liurole',
#    'hpp': 'true',
#    'ccy': 'OSC',
#    'ctc': 'ETH_BTC'
#    }
#    response = s.get('http://httpbin.org/cookies', cookies = cookies, headers = headers)
#    print(response.text)    
#
#    # 测试2
#    s = requests.Session()
#    s.get('http://httpbin.org/cookies/set/number/123456789')
#    response = s.get('http://httpbin.org/cookies')
#    print(response.text) 
    

    text = get_page_index(28)
    urls = parse_page_index(text)