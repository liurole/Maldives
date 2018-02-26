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

from selenium import webdriver

if __name__ == '__main__':
    
    option = webdriver.ChromeOptions()
    option.add_argument('--user-data-dir=' + 'C:/Users/Se/AppData/Local/Google/Chrome/User Data')
    driver = webdriver.Chrome(chrome_options = option)
    #driver.get('http://www.baidu.com')
    #driver.get('https://www.sekorm.com')
    driver.get('https://www.51lkh.com/game/home')
    







