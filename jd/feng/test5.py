#-*- coding:utf-8 -*-
'''
__author__ = 'Administrator'
'''
#主业务
class chongzhi(object):
    def chongqian(self,number):
        #滑动鼠标点击充值
        from selenium.webdriver.common.action_chains import ActionChains
        ActionChains(mybr).move_to_element(mybr.find_element_by_xpath("html/body/header/div[2]/div/div/div[2]/a")).perform()
        mybr.find_element_by_xpath("html/body/header/div[2]/div/div/div[2]/ul/li[1]/a").click()
        #输入金额
        mybr.find_element_by_xpath(".//*[@id='charge']").clear()
        mybr.find_element_by_xpath(".//*[@id='charge']").send_keys(number)
        #点击充值
        mybr.find_element_by_xpath(".//*[@id='incharge_done']").click()
        '''
        cur_1=mybr.current_window_handle()
        print(cur_1)
        handle1=mybr.window_handles
        print(handle1)

        for i in handles:
            if cur_1!=i:
                mybr.switch_to_window(i)
      '''
        #点击前往先锋支付
        mybr.find_element_by_xpath("html/body/div[1]/div[1]/section/div/div/p[2]/a").click()
        '''
        for i in handle1:
            if cur_1!=i:
                mybr.switch_to_window(i)
        '''
        #选择银行   有问题
        mybr.find_element_by_css_selector("value").value_of_css_property("CCB_1111010_01")
        #点击下一步
        mybr.find_element_by_xpath(".//*[@id='bankPayNext']").click()
        print(u"运行结束！")


if __name__=='__main__':
    import test3
    import test4
    O=test3.open1()
    mybr=O.dakai("http://www.firstp2p.com/")
    D=test4.denglu()
    D.login("hanshaofei","142730",mybr)
    C=chongzhi()
    C.chongqian("100")
