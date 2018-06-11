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

import requests
import re
import math

def get_data(assetid, isInit = True, step = 1000):
    headers = {
    'Cache-Control': 'no-cache',
    'Connection': 'Transfer-Encoding',
    'Connection': 'keep-alive',
    'Content-Security-Policy': 'default-src blob: data: https: \'unsafe-inline\' \'unsafe-eval\'; script-src \'self\' \'unsafe-inline\' \'unsafe-eval\' https://steamcommunity-a.akamaihd.net/ https://api.steampowered.com/ *.google-analytics.com https://www.google.com https://www.gstatic.com https://apis.google.com; object-src \'none\'; connect-src \'self\' https://api.steampowered.com/ https://store.steampowered.com/ wss://community.steam-api.com/websocket/ *.google-analytics.com http://127.0.0.1:27060 ws://127.0.0.1:27060; frame-src \'self\' steam: https://store.steampowered.com/ https://www.youtube.com https://www.google.com https://sketchfab.com https://player.vimeo.com;',
    'Content-Type': 'application/json; charset=utf-8',
    'Date': 'Sat, 26 May 2018 13:09:57 GMT',
    'Expires': 'Mon, 26 Jul 1997 05:00:00 GMT',
    'Server': 'Apache',
    'Strict-Transport-Security': 'max-age=3600',
    'Transfer-Encoding': 'chunked',
    'X-Frame-Options': 'SAMEORIGIN'
    }
    pre_url = 'https://steamcommunity.com/inventory/76561198129439885/570/2?l=schinese&count='
    if isInit:
        url = pre_url + str(step)
    else:
        url = pre_url + str(step) + '&start_assetid=' + assetid
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        return None
        
def cut(html):
    result =re.search('assets":\[(.*?)\],"descriptions', html, re.S)
    assets = result.group(1)
    result =re.search('descriptions":(.*)', html, re.S)
    descriptions = result.group()
    
    return assets, descriptions

def get_assets(assets):
    appid = re.findall('appid":(.*?),"contextid', assets, re.S)
    contextid = re.findall('contextid":"(.*?)","assetid', assets, re.S)
    assetid = re.findall('assetid":"(.*?)","classid', assets, re.S)
    classid = re.findall('classid":"(.*?)","instanceid', assets, re.S)
    instanceid = re.findall('instanceid":"(.*?)","amount', assets, re.S)
    amount = re.findall('amount":"(.*?)"}', assets, re.S)
    temp = {}
    temp['appid'] = appid
    temp['contextid'] = contextid
    temp['assetid'] = assetid
    temp['classid'] = classid
    temp['instanceid'] = instanceid
    temp['amount'] = amount

    return temp
    
def get_descriptions(descriptions):
    currency = re.findall('currency":(.*?),"background_color', descriptions, re.S)
    tradable = re.findall('tradable":(.*?),"name', descriptions, re.S)
    name = re.findall('"name":"(.*?)","name_color', descriptions, re.S)
    market_name = re.findall('market_name":"(.*?)","market_hash_name', descriptions, re.S)
    market_hash_name = re.findall('market_hash_name":"(.*?)","commodity', descriptions, re.S)
    commodity = re.findall('commodity":(.*?),"market_tradable_restriction', descriptions, re.S)
    market_tradable_restriction = re.findall('market_tradable_restriction":(.*?),"market_marketable_restriction', descriptions, re.S)
    market_marketable_restriction = re.findall('market_marketable_restriction":(.*?),"marketable', descriptions, re.S)
    marketable = re.findall('marketable":(.*?),"tags', descriptions, re.S)
    temp = {}
    temp['currency'] = currency
    temp['tradable'] = tradable
    temp['name'] = name
    temp['market_name'] = market_name
    temp['market_hash_name'] = market_hash_name
    temp['commodity'] = commodity
    temp['market_tradable_restriction'] = market_tradable_restriction
    temp['market_marketable_restriction'] = market_marketable_restriction
    temp['marketable'] = marketable
    
    return temp


if __name__ == '__main__':
    
    totalnum = 2400
    step = 1000
    isInit = True
    assetid = 'start'
    nums = math.ceil(totalnum / step)
    result = []
    
    for i in range(nums):
        if isInit:
            html = get_data(assetid, isInit, step)
            if html == None:
                print('运行错误！')
                break
            else:
                assets, descriptions = cut(html)
                assets = get_assets(assets)
                descriptions = get_descriptions(descriptions)
                temp = {}
                temp.update(assets)
                temp.update(descriptions)
                str_out = str(i * step) + ' to ' +  str(i * step + step) + 'Done!'
                print(str_out)
                result.append(temp)
                assetid = temp['assetid'][-1]
                isInit = False
        else:
            html = get_data(assetid, isInit, step)
            if html == None:
                print('运行错误！')
                break
            else:
                assets, descriptions = cut(html)
                assets = get_assets(assets)
                descriptions = get_descriptions(descriptions)
                temp = {}
                temp.update(assets)
                temp.update(descriptions)
                str_out = str(i * step) + ' to ' +  str(i * step + step) + 'Done!'
                print(str_out)
                result.append(temp)
                assetid = temp['assetid'][-1]





