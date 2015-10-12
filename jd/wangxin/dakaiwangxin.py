__author__ = 'jd'
#-*-coding:utf-8-*-
class Test(object):
    def Denglu(self):
        from selenium import webdriver
        www = webdriver.Firefox()
        www.maximize_window()
        www.get("http://www.firstp2p.com")
        return www

    def shuru(self):
        gg.find_element_by_name("username").send_keys("hanshaofei")
        gg.find_element_by_name("password").send_keys("142730")
        return gg