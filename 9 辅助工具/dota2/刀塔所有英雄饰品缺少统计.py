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

import pandas as pd

if __name__ == '__main__':
    
    # 读取Excel
    file = '刀塔所有英雄饰品名称.xlsx'
    result_web = pd.read_excel(file)
    file = '在线json库存管理.xlsx'
    result_own = pd.read_excel(file)
    name_own = result_own['市场英文名称'].tolist()
    
    # 创建一个空的 DataFrame  
    df_own = pd.DataFrame(columns=['拥有'])  
    
    for index in result_web.index:
        temp = result_web['物品名称'][index]
        if temp in name_own:
            df_own.loc[index] = 1
        else:
            df_own.loc[index] = 0
        
    result = pd.concat([result_web, df_own], axis=1)
    result.to_excel("刀塔所有英雄饰品缺少统计.xlsx", index=False)     # write data to excel
    