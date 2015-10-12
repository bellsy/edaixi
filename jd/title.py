__author__ = 'jd'
#-*- coding:utf-8 -*-

import unittest
from selenium import webdriver
class baogao():
    def html(self):
        import HTMLTestRunner
        lujing = "D:\\dd.html"
        lll = file(lujing,'wb')
        runnm = HTMLTestRunner.HTMLTestRunner(stream=lll,title=u'验证title',description=u'用例执行报告')
        runnm.run(myunit)
        lll.close()

class clicktitle(unittest.TestCase):
#clicktitle类继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。

    def setUp(self):
        self.liulanqi = webdriver.Firefox()
########加self 代表这个东西能被所有的def使用
        self.liulanqi.maximize_window()
        self.liulanqi.implicitly_wait(2)
########智能等待

    def tearDown(self):
        self.liulanqi.quit()

    def testbaidu(self):
        self.liulanqi.get('http://www.baidu.com')
        print self.liulanqi.title
########输出浏览器的title
        self.assertEqual(u'百度一下，你就知道',self.liulanqi.title)
########逗号之前预期结果，逗号之后实际结果

    def testwangxin(self):
        self.liulanqi.get('http://www.firstp2p.com/')
        print self.liulanqi.title
        self.assertEqual(u'网信理财',self.liulanqi.title)

    def testzshop(self):
        self.liulanqi.get('http://172.17.33.111:8019/iwebshop')
        print self.liulanqi.title
        self.assertEqual(u'iwebshop',self.liulanqi.title)

if __name__ == "__main__":
#unittest.main()
#unitest.main()函数用来测试 类中以test开头的测试用例
#放列表里面
    listcase = ['testbaidu','testwangxin']
#创建测试套
    myunit = unittest.TestSuite()
    for mycase in listcase:
        print mycase
        #将测试用例放入到测试容器中
        myunit.addTest(clicktitle(mycase))
#    unittest.TextTestRunner(verbosity=2).run(myunit)
#    unittest.TextTestRunner().run(myunit)
#  verbosity=2 所有case 分别的报告，不加括号里面的是放在一起
    baogao().html()


