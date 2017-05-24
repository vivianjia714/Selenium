#coding=utf-8
##验证基本查询功能-英国
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class query(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Firefox()
        self.verificationErrors = []

#打开院校库,根据学校名称进行查询-英国，输入学校关键字后进行查询，结果断言
    def test_query(self):
        u'''基本查询功能用例'''
        self.driver.get('http://www.jiemo.net/school')
        self.driver.maximize_window()
        self.driver.find_element_by_id("search_sh_name").send_keys(u"布里斯托大学")
        self.driver.find_element_by_xpath(".//*[@id='theform']/div[1]/div[1]/div/div[1]/div[2]/div/span/button").click()
        time.sleep(3)
        t1 = self.driver.find_element_by_xpath(".//*[@id='show_list']/div/div/div[2]/h3/a").text
        try:
            self.assertEqual(u'布里斯托大学',t1)

        except AssertionError as e:
            self.verificationErrors.append(str(e))
            
#切换国家-日本，选择大学，地区条件后，查询结果进行断言
        self.driver.find_element_by_xpath(".//*[@id='theform']/div[1]/div[1]/div/div[1]/div[3]/ul/li[3]/a").click()
        self.driver.find_element_by_id("dropdownMenu2").click()
        self.driver.find_element_by_xpath(".//*[@id='theform']/div[1]/div[1]/div/div[2]/div[2]/div[2]/ul/li[5]/a").click()
        t2 = self.driver.find_element_by_xpath(".//*[@id='show_list']/div[1]/div/div[2]/h3/a").text
        try:
            self.assertEqual(u'东京大学',t2)

#切换国家-日本，选择语言学校，查询结果进行断言
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            
        self.driver.find_element_by_xpath(".//*[@id='theform']/div[1]/div[1]/div/div[4]/div[2]/ul/li[2]/a").click()
        t3 = self.driver.find_element_by_xpath(".//*[@id='show_list']/div[8]/div/div[2]/h3/a").text
        try:
            self.assertEqual(u'早稻田EDU日本语学校',t3)

        except AssertionError as e:
            self.verificationErrors.append(str(e))
 
 
#切换国家-韩国，查询结果进行断言            
        self.driver.find_element_by_xpath(".//*[@id='theform']/div[1]/div[1]/div/div[1]/div[3]/ul/li[5]/a").click()
        t4 = self.driver.find_element_by_xpath(".//*[@id='show_list']/div[1]/div/div[2]/h3/a").text   
        try:
            self.assertEqual(u'首尔大学',t4)

        except AssertionError as e:
            self.verificationErrors.append(str(e))
            
            
#切换国家-澳洲，选择意向课程，专业方向
        self.driver.find_element_by_xpath(".//*[@id='theform']/div[1]/div[1]/div/div[1]/div[3]/ul/li[2]/a").click()    
        self.driver.find_elements_by_xpath(".//*[@id='dropdownMenu4']")[0].click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='theform']/div[1]/div[1]/div/div[5]/div[3]/div/ul/li[5]/a").click()
        self.driver.find_elements_by_xpath(".//*[@id='dropdownMenu4']")[1].click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='theform']/div[1]/div[1]/div/div[5]/div[4]/div/ul/li[3]/a").click()
        time.sleep(2)
        self.driver.save_screenshot('E:\\automation\\case_result\\case_screenshot\\result_query.png')
        
        
        
#切换国家-美国，
        self.driver.find_element_by_xpath(".//*[@id='theform']/div[1]/div[1]/div/div[1]/div[3]/ul/li[4]/a").click()
        self.driver.find_element_by_xpath(".//*[@id='theform']/div[1]/div[1]/div/div[5]/div[2]/ul/li[4]/a").click()
        self.driver.find_element_by_xpath(".//*[@id='theform']/div[1]/div[1]/div/div[6]/div[2]/ul/li[4]/a").click()  
        t5 = self.driver.find_element_by_xpath(".//*[@id='show_list']/div[4]/div/div[2]/h3/a").text   
        try:
            self.assertEqual(u'凯斯西储大学',t5)

        except AssertionError as e:
            self.verificationErrors.append(str(e))
        


    def tearDown(self):
        #self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()
   
       
if __name__ == "__main__": 
    unittest.main()