__author__ = 'jd'
#coding:utf-8
from selenium import webdriver
jubing = webdriver.Firefox()
jubing.get("http://www.12306.cn/mormhweb/")
print jubing.current_window_handle
jubing.find_element_by_xpath(".//*[@id='newLeft']/div[3]/a/img").click()
print jubing.window_handles
diyi = jubing.current_window_handle
dier = jubing.window_handles
#print jubing.current_window_handle# 当前句柄
#print jubing.window_handles# 所有句柄
for i in dier:
    if diyi != i:

#多层框架或窗口的定位：
#switch_to_frame()
#switch_to_window()
        jubing.switch_to_window(i)

        jubing.find_element_by_xpath(".//*[@id='classfied1']/ul/li/table/tbody/tr[1]/th/a").click()
        jubing.find_element_by_xpath(".//*[@id='agree']/span/ins").click()
        jubing.find_element_by_xpath(".//*[@id='nextPage']").click()
        jubing.switch_to_alert().text
        jubing.switch_to_alert().accept()  #弹出框拒接同意
#       jubing.switch_to_alert().dismiss() #弹出框拒接
#       jubing.switch_to_alert(). xxxxxxx  #回车
    else:
        print "jieshu"

        jubing.forward()
        jubing.back()
        jubing.title