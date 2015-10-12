__author__ = 'jd'
# -*- coding= utf-8 -*-

from selenium import webdriver
#打开浏览器 打开链接
myxiaohong = webdriver.Firefox()
myxiaohong.get("")
myxiaohong.implicitly_wait(6)
#最大化窗口
myxiaohong.maximize_window()
#实现登陆
myxiaohong.find_element_by_link_text("登录").click()
myxiaohong.find_element_by_id("phone").send_keys("")
myxiaohong.find_element_by_id("password").send_keys("")
myxiaohong.implicitly_wait(5)
myxiaohong.find_element_by_xpath(".//*[@id='loginBtn']").click()
myxiaohong.implicitly_wait(5)
#点击我要理财
myxiaohong.find_element_by_xpath(".//*[@id='navMenu']/li[2]/a").click()
myxiaohong.implicitly_wait(5)
#选择一个标的
for j in range(4,6):
    for i in range(1,8):
        bbb = myxiaohong.find_element_by_xpath(".//*[@id='loanList']/tr["+str(i)+"]/td[1]/a").text
        print bbb
        if bbb == u"借款测试111":
            print u"点击进入投资页面"
            myxiaohong.find_element_by_xpath(".//*[@id='loanList']/tr["+str(i)+"]/td[1]/a").click()
        else:
            print "0"
    print u"翻页"
    myxiaohong.find_element_by_xpath("html/body/div[3]/div/div[4]/a["+str(j)+"]").click()