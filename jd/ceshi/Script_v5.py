#-*-coding:utf-8-*-
__author__ = 'jd'
from selenium import webdriver
driver = webdriver.Firefox()
def login(rev_n,rev_p):

    driver.get("http://www.firstp2p.com/")
    driver.find_element_by_xpath("html/body/header/div[1]/div/ul/li[1]/a").click()
    driver.implicitly_wait(3)
    driver.find_element_by_id("user").send_keys(rev_n)
    driver.find_element_by_name("password").send_keys(rev_p)
    driver.find_element_by_xpath(".//*[@id='loginForm']/div/div[4]/div/input").click()

def re():
    driver.find_element_by_xpath("").send_keys()


if __name__ == '__main__':
    login()
