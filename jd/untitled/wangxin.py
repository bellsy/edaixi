#-*-coding:utf-8-*-
from selenium import webdriver
mingzi = webdriver.Firefox()
mingzi.get("http://www.firstp2p.com")
mingzi.find_element_by_xpath("/html/body/header/div/div/ul/li/a").click()
mingzi.find_element_by_name("username").send_keys("13810711525")
mingzi.find_element_by_name("password").send_keys("963852159qq")
mingzi.find_element_by_class_name("log-sprite").submit()
mingzi.find_element_by_link_text("P2P理财").click()
if mingzi.find_element_by_link_text(a) == "100起投，友居贷3号485-5"
    print mingzi.find_element_by_xpath("/html/body/div/section/div/div[2]/div/div/div[3]/div/div/div[2]/p/em/i").text
    #日期
mi


# a = "100起投，友居贷3号485-3"
# if a == mingzi.find_element_by_link_text("100起投，友居贷3号485-3"):
#     print mingzi.find_element_by_xpath("/html/body/div/section/div/div[2]/div/div/div/div/div/div[2]/p/em/i").text
# else:
#     print "nbbhh"


# cof = mingzi.find_element_by_xpath("html/body/div[1]/section/div/div[2]/div/div[1]/div[1]/div/div[1]/h3/a").click()
# coa = mingzi.find_element_by_xpath("html/body/div[1]/div/section[1]/div/div/div[2]/dl[2]/dt")
# print coa
#
# if con = cof:
#     print con
# else
#     print("he")


# mingzi.find_element_by_xpath("html/body/div[1]/section/div/div[2]/div/div[1]/div[2]/div/div[1]/h3/a")
# bbb = mingzi.find_element_by_xpath("html/body/div[1]/section/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/p[1]/em/i")
#
# if mingzi.find_element_by_xpath("html/body/div[1]/section/div/div[2]/div/div[1]/div[2]/div/div[1]/h3/a").text == "长兴1号213-16":
#     print ("html/body/div[1]/section/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/p[1]/em/i").text
# else:
#     print "hello"



#print mingzi.title
#打印title
# alo = html/body/div[1]/section/div/div[2]/div/div[1]/div[4]/div/div[1]/div[2]/p[1]/em/i
# if mingzi.find_element_by_link_text("100起投，e利宝039-27"):
#     print alo
# else:
#     print mingzi.title()
#	Result	Protocol	Host	URL	Body	Caching	Content-Type	Process	Comments	Custom