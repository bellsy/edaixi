__author__ = 'jd'

from selenium import webdriver
baidu = webdriver.Firefox()
baidu.get("https://www.baidu.com")
baidu.find_element_by_name("wd").send_keys("100")
baidu.find_element_by_id("su").click()
baidu.find_element_by_xpath(".//*[@id='2']/h3/a").click()