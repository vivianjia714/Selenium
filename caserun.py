#coding=utf-8
import unittest
import basic_query,enroll_test_detail,enroll_test_list,major_apply,school_detail_apply,school_list_apply,mail_send
#from jiemotest.login import testlogin
import HTMLTestRunner

testunit=unittest.TestSuite()

#将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(basic_query.query))
testunit.addTest(unittest.makeSuite(enroll_test_detail.enroll_detail))
testunit.addTest(unittest.makeSuite(enroll_test_list.enroll_list))
testunit.addTest(unittest.makeSuite(major_apply.major_apply))
testunit.addTest(unittest.makeSuite(school_list_apply.school_apply))
testunit.addTest(unittest.makeSuite(school_detail_apply.school_detail_apply))




#执行测试套件
runner = unittest.TextTestRunner()

#定义个报告存放路径，支持相对路径。
filename = 'E:\\automation\\case_result\\case_report\\result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title=u'院校库测试报告', description=u'用例执行情况：')

runner.run(testunit)
