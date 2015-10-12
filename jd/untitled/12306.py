__author__ = 'jd'
#coding:utf-8

from   import webdriver
tielu = webdriver.Firefox()
tielu.get("http://www.12306.cn/mormhweb/")
tielu.find_element_by_xpath(".//*[@id='newLeft']/div[3]/a/img").click()
tielu = driver.current_window_handle #获取当前窗口句柄
print tielu   #输出当前获取的窗口句柄