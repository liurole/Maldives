# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 22:03:08 2018

@author: Se

下载chromedrive驱动 
使用Selenium需要选择一个调用的浏览器并下载好对应的驱动，本文使用chrome浏览器，当然也可以用FireFox等
http://www.seleniumhq.org/download/ 找到Google Chrome Driver链接
对应驱动放在python目录下面的scripts目录中，例如C:\ProgramData\Anaconda3\envs\python35\Scripts
"""
# 可直接通过pip install 安装
import sys
import getopt
import difflib
import time
import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urlencode

def compare_str(first, second):
    seq = difflib.SequenceMatcher(lambda x: x in '-', first, second)  
    ratio = seq.ratio()
    return ratio  

# 利用request，导入cookies，header进行关键词网页搜索，选择第二栏
def check_repeated(keyword, tab = 0):
    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'tab': str(tab),
    }
    params = urlencode(data)
    base = 'https://www.sekorm.com/Web/Search/keyword/'
    url = base + keyword + '?' + params
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        return None

# 获取所有搜索结果链接，共100个
def get_all_urls(html):
    names = []
    urls = []
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('#zhuge_general a')
    if len(result) == 0:
        return names, urls
    else:
        for i in result:
            temp = i.get('href')
            urls.append(temp)
            temp = i.get_text()
            names.append(temp)
        return names, urls

# 搜索所有名称，看是否与该关键词类似
def search_all_urls(names, keyword, length = 20):
    length = min(length, len(names))
    ratio = 0.
    for i in range(length):
        temp = compare_str(keyword, names[i])
        ratio = max(ratio, temp)
    
    if ratio > 0.88:
        return True
    else:
        return False

# 查重汇总程序
def is_repeated(keyword):
    html = check_repeated(keyword)
    names, urls = get_all_urls(html)
    repeated = search_all_urls(names, keyword)  
    return repeated

# 利用request，导入cookies，header进行关键词网页搜索，选择第二栏
def check(url):
    try:
        response = requests.get(url)
        response.encoding="utf-8"
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        return None

# 获取页面信息
def search_url(url):
    html = check(url)
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('#newsptit .fontw')
    title = result[0].get_text()
    # 查重
    repeated = is_repeated(title)
    if repeated:
        return False
    # 日期
    date = re.sub("\D", "", url)
    date = date[:8]
    return title, date

# 提交单个系列产品，仅适用于新产品
def submit(browser, surl, url, title, factory, date):
    browser.get(surl)
    # 转载类型
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div/div/form/div[1]/div/div/div/div[2]/div/span/div/label[1]/span[1]/input').click()
    
    # 原文链接
    urls = browser.find_element_by_id('originalUrl')
    urls.send_keys(url)    
    
    # 标题
    stitle = browser.find_element_by_id('originalTitle')
    stitle.send_keys(title)    
    
    # 厂牌
    if factory == 'SiliconLabs':
        browser.find_element_by_id('brandCode').click()
        time.sleep(2)
        browser.find_element_by_id('brandCodetreeLeft_14_span').click()
        browser.find_element_by_id('brandCodeconfirmBtn').click() 
    elif factory == 'Rogers':
        browser.find_element_by_id('brandCode').click()
        time.sleep(2)
        browser.find_element_by_id('brandCodetreeLeft_13_span').click()
        browser.find_element_by_id('brandCodeconfirmBtn').click()   
    
    # 理由
    reason = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div/div/form/div[7]/div/div/div/div[2]/div/span/textarea')
    reason.send_keys(date)
    
    # 新产品类型
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div/div/form/div[8]/div/div/div/div[2]/div/span/div/label[1]/span[1]/input').click()
    
    # 查重
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div/div/form/div[9]/div/div/div/div/div/span/button[1]').click()
        
    return 1

# 帮助run Maldives6.3.0.py --help
# run Maldives6.3.0.py -f SiliconLabs -u http://www.eeworld.com.cn/qrs/article_2018042547518.html
if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hf:u:', [ 'help', 'factory=', 'url=' ])
    url = ''
    factory = ''

    # 入口函数，不明白怎么调用参数的可以看下
    for key, value in opts:
        if key in ['-h', '--help']:
            print('马尔代夫V6.3')
            print('参数定义：')
            print('-h, --help\t显示帮助')
            print('-f, --factory\t厂牌')
            print('-u, --url\t参考链接')
            sys.exit(0)
        if key in ['-f', '--factory']:
            factory = value
        if key in ['-u', '--url']:
            url = value
    
    if url == '' or factory == '':
        sys.exit()
        
    print('马尔代夫V6.3 function with: ' + '\t' + url) 
    
    title, date = search_url(url)
    if title == '':
        sys.exit()
    
    # 打开chorme
    surl = 'https://cms.sekorm.com/content/login'
    browser = webdriver.Chrome()
    browser.get(surl)
    
    # 输入验证码
    name = browser.find_element_by_id('mobile')
    name.send_keys('15244608508')
    password = browser.find_element_by_id('password')
    password.send_keys('liu875288')
    button = browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div/div/div/div[2]/form/div[3]/div/button')
    button.click()
    
    # 切换到提主题页面
    surl = 'https://cms.sekorm.com/content/nps/selfSubject/add'    
    submit(browser, surl, url, title, factory, date)
    
    