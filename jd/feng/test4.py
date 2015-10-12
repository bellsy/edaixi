#-*- coding:utf-8 -*-
'''
__author__ = 'Administrator'
'''
#登录
class denglu(object):
    def login(self,name,keys,driver):
        driver.find_element_by_xpath("html/body/header/div[1]/div/ul/li[1]/a").click()
        driver.find_element_by_xpath(".//*[@id='user']").send_keys(name)
        driver.find_element_by_xpath(".//*[@id='input-password']").send_keys(keys)
        driver.find_element_by_xpath(".//*[@id='loginForm']/div/div[4]/div/input").click()
'''
if __name__=='__main__':
    import test3
    O=test3.open1()
    driver=O.dakai("http://www.firstp2p.com/")
    D=denglu()
    D.login("hanshaofei","142730")
    print(u"登录成功！")
'''