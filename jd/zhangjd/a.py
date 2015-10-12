__author__ = 'jd'
#-*-coding:utf-8*-

class Kuangjia(object):
    def web(self,wangzhan):
        from selenium import webdriver
        www = webdriver.Firefox()
        www.get(wangzhan)
        www.maximize_window()
        www.find_element_by_xpath()
        return www
    #
    # def denglu(self,zhanghao,mima,dakai):
    #     dakai.find_element_by_xpath("/html/body/header/div/div/ul/li/a").click()
    #     dakai.find_element_by_name("username").send_keys("zhanghao")
    #     dakai.find_element_by_name("password").send_keys("mima")
    #     dakai.find_element_by_xpath(".//*[@id='loginForm']/div/div[4]/div/input").click()
    #     return mima
    #     return zhanghao
    #
