__author__ = 'jd'
import test5_1
B = test5_1.Browser()
L = test5_1.Login()
M = test5_1.Mycount()
B.Initbrowser("http://www.firstp2p.com/")
L.login_p2p("hanshaofei","142730")
M.mycount()
B.closeBrowser(