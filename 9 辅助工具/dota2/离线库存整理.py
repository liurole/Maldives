# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:44:45 2018

@author: Se

这里主要考虑steam总是大姨妈，效果不好，所以暂时不管在线了
方法说明：
离线缓存文件夹下有个以数字开头的文件夹，将数据保存进入
貌似每次只能调取最多5000库存，因而需要多次保存
当前库存为7342，需要调用两次，因而文件分别保存为1.txt与2.txt
数据来源如下
第一次浏览器直接输入
https://steamcommunity.com/inventory/76561198129439885/570/2?l=schinese&count=5000
将所得数据保存至1.txt，做好心理准备，容易卡死，数据太多
该文件搜索],"descriptions":[      找到之前的"assetid":"11744278020"
第二次浏览器直接输入
https://steamcommunity.com/inventory/76561198129439885/570/2?l=schinese&count=5000&start_assetid=11744278020     
将所得数据保存至2.txt，做好心理准备，容易卡死，数据太多
库存不到一万，因而只需要两次，而且不用担心重复问题

"""

import os  
import re

def read_data(index):
    filedir = './离线缓存/' + str(index) + '/'
    files = os.listdir(filedir) #列出文件夹下所有的目录与文件
    data = []
    for i in files:
        file = filedir + i
        temp = open(file, 'r', encoding='UTF-8')
        data.append(temp.read())
    
    if len(data) > 0:
        return data

def cut(data):
    result =re.search('assets":\[(.*?)\],"descriptions', data, re.S)
    assets = result.group(1)
    result =re.search('descriptions":(.*)', data, re.S)
    descriptions = result.group()
    
    return assets, descriptions

def get_assets(assets):
    data = []
    content = re.findall('{"(.*?)"}', assets, re.S)
    for i in content:
        appid = re.search('appid":(.*?),"contextid', i, re.S)
        contextid = re.search('contextid":"(.*?)","assetid', i, re.S)
        assetid = re.search('assetid":"(.*?)","classid', i, re.S)
        classid = re.search('classid":"(.*?)","instanceid', i, re.S)
        instanceid = re.search('instanceid":"(.*?)","amount', i, re.S)
        amount = re.search('amount":"(.*)', i, re.S)
        temp = {}
        if appid == None:
            temp['appid'] = 'NULL'
        else:
            temp['appid'] = appid.group(1)
        if contextid == None:
            temp['contextid'] = 'NULL'
        else:
            temp['contextid'] = contextid.group(1)
        if assetid == None:
            temp['assetid'] = 'NULL'
        else:
            temp['assetid'] = assetid.group(1)
        if classid == None:
            temp['classid'] = 'NULL'
        else:
            temp['classid'] = classid.group(1)
        if instanceid == None:
            temp['instanceid'] = 'NULL'
        else:
            temp['instanceid'] = instanceid.group(1)
        if amount == None:
            temp['amount'] = 'NULL'
        else:
            temp['amount'] = amount.group(1)
            
        data.append(temp)

    return data
    
def get_descriptions(descriptions):
    data = []
    content = re.findall('{"(.*?)"}', descriptions, re.S)
    for i in content:
        
    
    
    currency = re.findall('currency":(.*?),"background_color', descriptions, re.S)
    tradable = re.findall('tradable":(.*?),"name', descriptions, re.S)
    name = re.findall('name":(.*?),"name_color', descriptions, re.S)
    types = re.findall('type":(.*?),"market_name', descriptions, re.S)
    market_name = re.findall('market_name":(.*?),"market_hash_name', descriptions, re.S)
    market_hash_name = re.findall('market_hash_name":(.*?),"commodity', descriptions, re.S)
    commodity = re.findall('commodity":(.*?),"market_tradable_restriction', descriptions, re.S)
    market_tradable_restriction = re.findall('market_tradable_restriction":(.*?),"market_marketable_restriction', descriptions, re.S)
    market_marketable_restriction = re.findall('market_marketable_restriction":(.*?),"marketable', descriptions, re.S)
    marketable = re.findall('marketable":(.*?),"tags', descriptions, re.S)
    temp = {}
    temp['currency'] = currency
    temp['tradable'] = tradable
    temp['name'] = name
    temp['types'] = types
    temp['market_name'] = market_name
    temp['market_hash_name'] = market_hash_name
    temp['commodity'] = commodity
    temp['market_tradable_restriction'] = market_tradable_restriction
    temp['market_marketable_restriction'] = market_marketable_restriction
    temp['marketable'] = marketable
    
    return temp


if __name__ == '__main__':
    
    index = 1
    result = []
    
    data = read_data(index)
    for i in data:
        assets, descriptions = cut(i)
        assets = get_assets(assets)
        descriptions = get_descriptions(descriptions)
        temp = {}
        temp.update(assets)
        temp.update(descriptions)
        result.append(temp)     
    




