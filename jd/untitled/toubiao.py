__author__ = 'jd'
#coding:utf-8
from selenium import webdriver
import time
toubiao = webdriver.Firefox()
toubiao.get("http://www.firstp2p.com")
time.sleep(4)
#toubiao.implicitly_wait(3) ���ܵȴ�
toubiao.find_element_by_xpath("/html/body/header/div/div/ul/li/a").click()
toubiao.find_element_by_name("username").send_keys("hanshaofei")
toubiao.find_element_by_name("password").send_keys("142730")
toubiao.find_element_by_class_name("log-sprite").submit()
toubiao.find_element_by_link_text("                                 P2P���                            ").click()
toubiao.find_element_by_link_text("100��Ͷ����ӯ3��046-1").click()
toubiao.title("���ڴ� - 100��Ͷ����ӯ3��046-1 - �������")
