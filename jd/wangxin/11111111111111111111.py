__author__ = 'jd'
#coding:utf-8
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