__author__ = 'jd'
#-*- coding:UTF-8 -*-

def
from selenium import webdriver
wuliu = webdriver.Firefox()

def login(zhanghao,mima):
    wuliu.get("http://wuliu.edaixi.com/")
    wuliu.find_element_by_class_name("btn-success").click()
    wuliu.find_element_by_id("username-container").send_keys(zhanghao)
    wuliu.find_element_by_id("password-container").send_keys(mima)
    wuliu.find_element_by_id("login-submit").click()