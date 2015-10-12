#-*- coding:UTF-8 -*-
#查询提现记录
class Browser(object):
    def Initbrowser(self,ret_url):
        global wangxw
        from selenium import webdriver     
        wangxw=webdriver.Firefox()
        wangxw.maximize_window()
        wangxw.get(ret_url)
        #self.mydir = wangxw
        #return self.mydir
        return wangxw
    
    def closeBrowser(self):
        #self.mydir.quit()
        wangxw.quit()
        
class Login(object):
    def login_p2p(self,name,password):
        #Browser.Initbrowser(self, "http://www.firstp2p.com/")
        wangxw.find_element_by_link_text("登录").click()
        wangxw.find_element_by_id("user").send_keys(name)
        wangxw.find_element_by_name("password").send_keys(password)
        wangxw.find_element_by_xpath(".//*[@id='loginForm']/div/div[4]/div/input").click()
        
class Mycount(object):
    def mycount(self):
        #导入包      
        from selenium.webdriver.common.action_chains import ActionChains
        #定义悬浮框的位置 
        a = wangxw.find_element_by_xpath("html/body/header/div[2]/div/div/div[2]/a")
        #执行移动到某一个悬浮框上的操作
        ActionChains(wangxw).move_to_element(a).perform()
        wangxw.find_element_by_xpath("html/body/header/div[2]/div/div/div[2]/ul/li[2]/a").click()
        wangxw.find_element_by_xpath(".//*[@id='dateInput1']").send_keys("2015-09-19")
        #wangxw.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[7]/a").click()
        wangxw.find_element_by_xpath(".//*[@id='dateInput2']").send_keys("2015-09-19")
        #wangxw.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[7]/a").click()
        wangxw.find_element_by_xpath(".//*[@id='search']/div/input[2]").click()

if __name__ == "__main__":
    #方法一：
    #===========================================================================
    # B = Browser()
    # L = Login()
    # M = Mycount()
    # 
    # B.Initbrowser("http://www.firstp2p.com/")
    # L.login_p2p("hanshaofei","142730")
    # M.mycount()
    # B.closeBrowser()
    #===========================================================================
    #方法二：
    Browser().Initbrowser("http://www.firstp2p.com/")
    Login().login_p2p("hanshaofei","142730")
    Mycount().mycount()
    Browser().closeBrowser()
