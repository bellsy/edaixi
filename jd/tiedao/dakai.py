__author__ = 'jd'
#coding:utf-8
def dakaitiedao():
    from selenium import webdriver
    wangzhan = webdriver.Firefox()
    url = "http://www.12306.cn/mormhweb/"
    wangzhan.get(url)
    return wangzhan
if __name__ == '__main__':
    dakaitiedao()
