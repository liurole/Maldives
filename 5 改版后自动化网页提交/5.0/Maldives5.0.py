# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:26:50 2017

@author: Se

马尔代夫V5.0

实现了网页的自动输入

run Maldives5.0.py
"""

"""
1.安装Selenium 
pip install selenium

2.下载chromedrive驱动 
使用Selenium需要选择一个调用的浏览器并下载好对应的驱动，本文使用chrome浏览器，当然也可以用FireFox等
http://www.seleniumhq.org/download/ 找到Google Chrome Driver链接
对应驱动放在python目录下面的scripts目录中，例如C:\ProgramData\Anaconda3\envs\python35\Scripts
注：如果是macOS，下载对应版本驱动解压到环境变量包含的路径即可，比如/usr/local/bin

3.需要注意的是，验证后一定要手工点击一下，否则我这里会出现重复验证
"""

from selenium import webdriver
import time

# 打开chorme
bolgurl = 'https://cms.sekorm.com/snps/'
browser = webdriver.Chrome()
browser.get(bolgurl)

# 输入验证码
name = browser.find_element_by_id('code')
name.send_keys('zneWR56ylKQ1Pvtn')

# 点击确定，加载完成后等待4秒（网页设定为3s）
login_button = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div[1]/form/div[3]/div/div/div/div/button')
login_button.click()
time.sleep(4)
# browser.implicitly_wait(4)

pick = input("是否已访问刷新页面？ y/n:")

if pick == 'y':
    # 标题输入
    my_title = u'【产品】牛逼哥的标题'
    name = browser.find_element_by_id('title')
    name.send_keys(my_title)
    
    # 新产品
    browser.find_element_by_name('acticleType').click()
    
    # 摘要
    my_abstract = u'牛逼哥摘要'
    name = browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[2]/form/div[4]/div[1]/div/div/div[2]/div/textarea')
    name.send_keys(my_abstract )
    
    # 器件名称
    my_name = u'牛逼哥的名称'
    name = browser.find_element_by_id('goodKeyword')
    name.send_keys(my_name)
    
    # 型号
    my_type = u'牛逼哥的型号'
    name = browser.find_element_by_id('pnKeyword')
    name.send_keys(my_type)
    
    # 市场应用
    my_app = u'牛逼哥的应用'
    name = browser.find_element_by_id('elecKeyword')
    name.send_keys(my_app)
    
    # 关键词
    my_key = u'牛逼哥关键词'
    name = browser.find_element_by_id('keyword')
    name.send_keys(my_key)
    
    # 作者姓名
    my_id = u'牛逼哥的ID'
    name = browser.find_element_by_id('writer')
    name.send_keys(my_id)
    
    # 笔名
    my_author = u'牛逼哥的姓名'
    name = browser.find_element_by_id('author')
    name.send_keys(my_author)
    
    # 参考链接
    my_ref = u'牛逼哥的文献'
    name = browser.find_element_by_id('referLink')
    name.send_keys(my_ref)
    
    # 厂牌（这里选京瓷）
    browser.find_element_by_id('brandCode').click()
    browser.find_element_by_id('brandCodetreeLeft_47_span').click()
    browser.find_element_by_id('brandCodeconfirmBtn').click()
    
    # 正文输入
    my_content = u'牛逼哥第一段\n牛逼哥第二段'
    browser.switch_to.frame('ueditor_0')  # 注意，这种editor一定有frame，一定要切frame
    browser.find_element_by_tag_name('body').send_keys(my_content)
    browser.switch_to.default_content()
    
    # 预览
    login_button = browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[2]/form/div[16]/div/div/div/div/div/button[2]')
    login_button.click()
else:
    pass
