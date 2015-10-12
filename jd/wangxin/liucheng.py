__author__ = 'jd'
#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
toubiao = webdriver.Firefox()
toubiao.get("http://www.firstp2p.com")
toubiao.maximize_window()
toubiao.find_element_by_xpath("/html/body/header/div/div/ul/li/a").click()
toubiao.find_element_by_name("username").send_keys("hanshaofei")
toubiao.find_element_by_name("password").send_keys("142730")
toubiao.find_element_by_xpath(".//*[@id='loginForm']/div/div[4]/div/input").click()
a = toubiao.find_element_by_xpath("html/body/header/div[2]/div/div/div[2]/a")
ActionChains(toubiao).move_to_element(a).perform()
toubiao.find_element_by_xpath("html/body/header/div[2]/div/div/div[2]/ul/li[2]/a").click()
toubiao.find_element_by_xpath(".//*[@id='search']/div/div[1]/div").click()
toubiao.find_element_by_xpath(".//*[@id='search']/div/div[1]/ul/li[2]").click()
time.sleep(5)
toubiao.find_element_by_xpath(".//*[@id='dateInput1']").send_keys("2014-04-03")
time.sleep(5)
toubiao.find_element_by_xpath(".//*[@id='dateInput2']").send_keys("2015-09-01")
time.sleep(5)
toubiao.find_element_by_xpath(".//*[@id='search']/div/input[2]").click()
time.sleep(5)
print (toubiao.find_element_by_xpath("html/body/div[1]/div[3]/section/div/div/table/tbody/tr/td[1]").text)
print toubiao.find_element_by_xpath("html/body/div[1]/div[3]/section/div/div/table/tbody/tr/td[2]").text
print toubiao.find_element_by_xpath("html/body/div[1]/div[3]/section/div/div/table/thead/tr/th[3]").text
print toubiao.find_element_by_xpath("html/body/div[1]/div[3]/section/div/div/table/tbody/tr/td[4]").text
print toubiao.find_element_by_xpath("html/body/div[1]/div[3]/section/div/div/table/tbody/tr/td[5]/div").text


mydriver.execute_script("document.getElementById('dateInput1').setAttribute('value','2015-03-12')")

V1111111111111111111111111111111
import unittest
class jisuan(unittest.TestCase):
    def setUp(self):
        print u"开始计算"

    def tearDown(self):
        print u"清理推出"

    def testsum(self):
        print 2 + 3

    def testjian(self):
        print 23 - 1
if __name__ == "__main__":
    unittest.main()



V2222222222222222222222222222222

import unittest
class jisuan(unittest.TestCase):
    def setUp(self):
        print u"开始计算"

    def tearDown(self):
        print u"清理推出"

    def testsum(self):
        print 2 + 3

    def testjian(self):
        print 23 - 1
if __name__ == "__main__":
    unittest.main



V333333333333333333333333

import unittest
class jisuan(unittest.TestCase):
    def setUp(self):
        print u"开始计算"

    def tearDown(self):
        print u"清理推出"

    def testsum(self):
        print 2 + 3

    def testchufa(self):
        print 21 / 7

    def testjchengfa(self):
        print 23 * 2
if __name__ == "__main__":

    unittest.main