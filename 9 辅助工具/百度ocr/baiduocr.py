# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 10:51:15 2018

@author: Se
"""

from aip import AipOcr

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

if __name__ == '__main__':
    
    """ 你的 APPID AK SK """
    APP_ID = '10908314'
    API_KEY = 'iXrjEUHP8kwRuFtm5RvHkPFx'
    SECRET_KEY = 'NIxuFEaGbgYO3A4AAhtBcpbihuHw1BQK'
    
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    
    image = get_file_content('test1.jpg')
    
    """ 调用通用文字识别（高精度版） """
    client.basicAccurate(image);
    
    """ 如果有可选参数 """
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "true"
    
    """ 带参数调用通用文字识别（高精度版） """
    client.basicAccurate(image, options)
    
    