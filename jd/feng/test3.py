#-*- coding:utf-8 -*-
'''
__author__ = 'Administrator'
'''
#打开浏览器
class open1(object):
    def dakai(self,url):
        from selenium import webdriver
        browser=webdriver.Firefox()
        browser.get(url)
        browser.maximize_window()
        return browser
'''
if __name__=='__main__':
    open1().dakai("http://www.firstp2p.com/")
'''
