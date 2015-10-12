__author__ = 'jd'
#-*- coding:utf-8 -*-
import tiedao.dakai
dianji = tiedao.dakai.dakaitiedao()
dianji.find_element_by_xpath(".//*[@id='newLeft']/div[3]/a/img").click()
print(dianji.current_window_handle)