#-*- coding:utf-8 -*-
class Mybrowser(object):
    def start(self,url):
        print u"打开浏览器"
        global driver
        from selenium import webdriver
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        handle1 = driver.current_window_handle
        print handle1
        return handle1

    def close(self):
        print u"关闭浏览器"
        driver.quit()

class Usrlogin():
    def login(self,username,password):
        print u"登录"
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath("//input[@type='submit']").click()
        return driver,username,password

    def charge(self):
        print u"充值"
        driver.find_element_by_link_text("我的账户").click()
        driver.find_element_by_class_name("button_cz").click()
        driver.find_element_by_id("charge").clear()
        driver.find_element_by_id("charge").send_keys("100")
        driver.find_element_by_id("incharge_done").click()
        driver.find_element_by_class_name("pay_button").click()

    def handle(self,handle1):
        print u"切换页面"
        all_handle = driver.window_handles
        for handle2 in all_handle:
            if handle2 != handle1:
                driver.switch_to_window(handle2)
                driver.implicitly_wait(10)

class Bank(object):
    def qingdaobank(self):
        print u"选择青岛银行"
        driver.find_element_by_xpath("/[14]/label/input").click()
        driver.find_element_by_id("bankPayNext").click()
        driver.find_element_by_xpath("html/bodyction/div/div[4]/form/div/input[3]").click()
        driver.find_element_by_id("BOC").click()
        driver.find_element_by_id("btnPay").click()

if __name__ == '__main__':
    myurl="http://www.firstp2p.com/"
    x = Mybrowser().start(myurl)
    Usrlogin().login("hanshaofei","142730")
    Usrlogin().charge()
    Usrlogin().handle(x)
    Bank().qingdaobank()
    Mybrowser().close()
