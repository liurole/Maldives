# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

马尔代夫V6.3.0

实现了对于指定网页集合的批量信息抓取

"""
import re
import difflib
import requests
import openpyxl
from bs4 import BeautifulSoup

# 利用request，导入cookies，header进行关键词网页搜索，选择第二栏
def get_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        return None

def select(html):
    data = []
    soup = BeautifulSoup(html, 'lxml')
    table_content = soup.select("td")
    for i, val in enumerate(table_content):
        if i % 11 == 10:
            temp = {}
            temp['name'] = table_content[i - 10].get_text()
            content = table_content[i - 10]
            result = re.search('\'page\': \'./(.*?)\', \'title\'', str(content), re.S)
            if result is None:
                temp['url'] = ''
            else:
                temp['url'] = 'http://prdct-search.kyocera.co.jp/function/' + result.group(1)
            temp['VRRM'] = table_content[i - 9].get_text()
            temp['IO'] = table_content[i - 8].get_text()
            temp['IFSM'] = table_content[i - 7].get_text()
            temp['IR'] = table_content[i - 6].get_text()
            temp['VFM'] = table_content[i - 5].get_text()
            temp['Tstg'] = table_content[i - 4].get_text()
            temp['Outline'] = table_content[i - 3].get_text()
            temp['Circuit'] = table_content[i - 2].get_text()
            temp['AEC-Q101'] = table_content[i - 1].get_text()
            temp['State'] = table_content[i].get_text()
            data.append(temp)
            
    return data

def compare_str(first, second):
    seq = difflib.SequenceMatcher(lambda x: x in '-', first, second)  
    ratio = seq.ratio()
    return ratio    

if __name__ == '__main__':
    
    url = 'http://prdct-search.kyocera.co.jp/function/datasheet.php?lang=zh&productNo=01'
    html = get_url(url)
    data = select(html)
    
    type_id = 1
    for i, val in enumerate(data):
        if i == 0:
            val['type'] = type_id
        else:
            ratio = compare_str(data[i - 1]['name'], data[i]['name'])
            if ratio < 0.85:
                type_id += 1
            val['type'] = type_id
            
    wb_out = openpyxl.Workbook()
    ws_out = wb_out.active
    ws_out.title = '京瓷肖特基'
    ws_out['A1'] = '序号'
    ws_out['B1'] = '类型'
    ws_out['C1'] = 'name'
    ws_out['D1'] = 'VRRM'
    ws_out['E1'] = 'IO'
    ws_out['F1'] = 'IFSM'
    ws_out['G1'] = 'IR'
    ws_out['H1'] = 'VFM'
    ws_out['I1'] = 'Tstg'
    ws_out['J1'] = 'Outline'
    ws_out['K1'] = 'Circuit'
    ws_out['L1'] = 'AEC-Q101'
    ws_out['M1'] = 'State'
    ws_out['N1'] = 'url'
    ws_out['O1'] = 'post'
    
    index = 2
    for i in data:
        temp = 'A' + str(index)
        ws_out[temp] = index - 1
        temp = 'B' + str(index)
        ws_out[temp] = i['type']
        temp = 'C' + str(index)
        ws_out[temp] = i['name']
        temp = 'D' + str(index)
        ws_out[temp] = i['VRRM']
        temp = 'E' + str(index)
        ws_out[temp] = i['IO']
        temp = 'F' + str(index)
        ws_out[temp] = i['IFSM']
        temp = 'G' + str(index)
        ws_out[temp] = i['IR']
        temp = 'H' + str(index)
        ws_out[temp] = i['VFM']
        temp = 'I' + str(index)
        ws_out[temp] = i['Tstg']
        temp = 'J' + str(index)
        ws_out[temp] = i['Outline']
        temp = 'K' + str(index)
        ws_out[temp] = i['Circuit']
        temp = 'L' + str(index)
        ws_out[temp] = i['AEC-Q101']
        temp = 'M' + str(index)
        ws_out[temp] = i['State']
        temp = 'N' + str(index)
        ws_out[temp] = i['url']
        temp = 'O' + str(index)
        ws_out[temp] = 0
        
        index += 1

    wb_out.save('京瓷肖特基汇总.xlsx')   
    