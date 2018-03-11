# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 11:22:18 2018

@author: Se

本程序不好使
目前官网例程有问题，不好使，而且貌似百度的确很牛逼
"""

import requests
import hashlib
import random
import base64

appKey = '68a68ddaf01f7b2f'
secretKey = 'AQwzCoZjhpMNVZApqUb9PWEghKv9eBLD'

httpClient = None


f=open(r'test1.jpg','rb') #二进制方式打开图文件
img=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()

detectType = '10012'
imageType = '1'
langType = 'ch'
salt = str(random.random())

sign = appKey + str(img) + salt + secretKey
md5 = hashlib.md5()
md5.update(sign.encode('UTF-8'))
sign = md5.hexdigest()
url = 'http://openapi.youdao.com/ocrapi'
data = {'appKey':appKey,'img':img,'detectType':detectType,'imageType':imageType,'langType':langType,'salt':str(salt),'sign':sign}

try:
    r = requests.get(url, params = data, timeout = 100)
except:
    print('error')

result = r.json()
  


