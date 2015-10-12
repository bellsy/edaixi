__author__ = 'jd'
#-*-coding:utf-8-*-


import MySql
class denglu():
    def login(self):
        global dever
        from selenium import webdriver
        dever = webdriver.Firefox()
        dever.get("http://172.17.33.111:8019/iwebshop")
        dever.maximize_window()
        dever.implicitly_wait(3)
        dever.find_element_by_xpath('html/body/div[1]/div[1]/p/a[1]').click()
        dever.find_element_by_xpath('html/body/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td/input').send_keys("test")
        dever.find_element_by_xpath('html/body/div[1]/div[2]/div/div/form/table/tbody/tr[2]/td/input').send_keys("zhang126")
        dever.find_element_by_xpath('html/body/div[1]/div[2]/div/div/form/table/tbody/tr[5]/td[2]/input').click()
        dever.find_element_by_xpath("html/body/div[1]/div[5]/div[1]/div[5]/div[2]/ul/li[1]/a").click()

    def address(self):
#
#        dever.find_element_by_xpath(".//*[@id='address_form']/form/table/tbody/tr[1]/td/input[2]").send_keys("但你")
# 也可以用以下方法下拉框选择
# listprovince=driver.find_element_by_xpath(".//*[@id='province']")
#        listprovince.find_element_by_xpath("//option[@value='42']").click()
#        driver.implicitly_wait(2)


        select1 = dever.find_element_by_id("province")
        zidingyibianliang1 = select1.find_elements_by_tag_name("option")
        for addr in zidingyibianliang1:
            addid = addr.get_attribute("value")
            if addid == "814":
                print addid
                addr.click

        select2 = dever.find_element_by_id("province")
        zidingyibianliang2 = select2.find_elements_by_tag_name("option")
        for myciti in zidingyibianliang2:
            addid2 = myciti.get_attribute("value")
            if addid2 == "926":
                print addid2
                addr2.click

        select3 = dever.find_element_by_id("province")
        zidingyibianliang3 = select3.find_elements_by_tag_name("option")
        for xiaodifang in zidingyibianliang3:
            addid3 = xiaodifang.get_attribute("value")
            if addid3 == "814":
                print addid3
                addr3.click



    def checkdata(self):
        pass

if __name__ == '__main__':
    denglu().login()
    denglu().address()

























# import unittest
# from selenium import webdriver
#
# class gouwu(unittest.TestCase):
#     def dakaiwangzhan(self):
#         self.liulanqi = webdriver.Firefox()
#         self.liulanqi.get('http://172.17.33.111:8019/iwebshop')
#         self.liulanqi.find_element_by_xpath('html/body/div[1]/div[1]/p/a[1]').click()
#         self.liulanqi.find_element_by_xpath('html/body/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td/input').send_keys("test")
#         self.liulanqi.find_element_by_xpath('html/body/div[1]/div[2]/div/div/form/table/tbody/tr[2]/td/input').send_keys("zhang126")
#         self.liulanqi.find_element_by_xpath('html/body/div[1]/div[2]/div/div/form/table/tbody/tr[5]/td[2]/input').click()
#         self.liulanqi.find_element_by_xpath("html/body/div[1]/div[5]/div[1]/div[5]/div[2]/ul/li[1]/a").click()
#         self.liulanqi.find_element_by_xpath(".//*[@id='address_form']/form/table/tbody/tr[1]/td/input[2]").send_keys("但你")
#         self.liulanqi.find_elements_by_id("province")
#         chengshi = self.liulanqi.find_elements_by_tag_name("option")
#         for addr in chengshi:
#             addid = addr.get_attribute("value")
#             print addr.text
#             if addid == "814":
#                 addr.click()
#
#         self.liulanqi.find_elements_by_id("city")
#         diqu = self.liulanqi.find_elements_by_tag_name("option")
#         for addr2 in diqu:
#             addid = addr.get_attribute("value")
#             print addr.text
#             if addid2 == "926":
#                 addr.click()
#
# # chengshi = self.liulanqi.find_elements_by_id("province")
# # biaoqian = self.liulanqi.find_elements_by_tag_name("option")
# # for addr in biaoqian:
# # addid = addr.get_attribute("value")
# # print addr.text
# # if addid == "814":
# # addr.click()
# #定位一个下拉框
#         self.liulanqi.find_element_by_xpath(".//*[@id='address_form']/form/table/tbody/tr[3]/td/input").send_keys("酒仙桥亲亲亲亲")
#         self.liulanqi.find_element_by_xpath(".//*[@id='address_form']/form/table/tbody/tr[4]/td/input").send_keys("100000")
#         self.liulanqi.find_element_by_xpath(".//*[@id='address_form']/form/table/tbody/tr[8]/td/label/input").click()
#
