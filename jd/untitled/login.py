#-*-coding:utf-8-*-
def denglu(rev_x,rev_y):
    from selenium import webdriver
    mingzi = webdriver.Firefox()
    mingzi.get("http://www.firstp2p.com")
    mingzi.find_element_by_xpath("/html/body/header/div/div/ul/li/a").click()
    mingzi.find_element_by_name("username").send_keys("rev_x")
    mingzi.find_element_by_name("password").send_keys("rev_y")
    mingzi.find_element_by_class_name("log-sprite").submit()