# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:28:47 2017

@author: Se

为小号而生

"""

import time
from selenium import webdriver

if __name__ == '__main__':
    
    # 打开chorme
    bolgurl = 'https://www.marlow.com/products/thermoelectric-coolers/single-stage'
    browser = webdriver.Chrome()
    browser.get(bolgurl)
    
    names = browser.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "product-header", " " ))]')

    #获取当前窗口句柄  
    now_handle = browser.current_window_handle  
    print(now_handle)

    # 测试第一个
    #print(names[0].text)
    names[0].click()
    # 获取所有窗口句柄    
    all_handles = browser.window_handles    
    # 弹出两个界面,跳转到不是主窗体界面    
    for handle in all_handles:    
        if handle!=now_handle:       
            # 输出待选择的窗口句柄    
            print(handle)    
            browser.switch_to_window(handle)    
            time.sleep(1)    
    
            print(u'弹出界面信息')    
            print(browser.current_url)
            print(browser.title)
    
#                #获取登录连接信息    
#                elem_p = browser.find_element_by_xpath("//div[@class='coltop clearfix']/div[2]")    
#                print(elem_p.text)     
    
            #关闭当前窗口    
            browser.close()    
                
    #输出主窗口句柄    
    print(now_handle)    
    browser.switch_to_window(now_handle) #返回主窗口 开始下一个跳转    
    

    types = []
    for i in names:
        types.append(i.text)
        #print(i.text)
        
        i.click()

        # 获取所有窗口句柄    
        all_handles = browser.window_handles    
        # 弹出两个界面,跳转到不是主窗体界面    
        for handle in all_handles:    
            if handle!=now_handle:       
                # 输出待选择的窗口句柄    
                print(handle)    
                browser.switch_to_window(handle)    
                time.sleep(1)    
        
                print(u'弹出界面信息')    
                print(browser.current_url)
                print(browser.title)
        
#                #获取登录连接信息    
#                elem_p = browser.find_element_by_xpath("//div[@class='coltop clearfix']/div[2]")    
#                print(elem_p.text)     
        
                #关闭当前窗口    
                browser.close()    
                    
        #输出主窗口句柄    
        print(now_handle)    
        browser.switch_to_window(now_handle) #返回主窗口 开始下一个跳转     

