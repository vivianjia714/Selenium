#coding=utf-8
#申请该学校-PC列表页
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class school_apply(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Firefox()
        self.verificationErrors = []
#打开院校库，用户登录         
    def test_school_apply(self):
        u'''申请该学校-pc端列表页'''
        self.driver.get('http://www.jiemodou.net/school')
        self.driver.maximize_window()
        nowhandle=self.driver.current_window_handle
        #print self.driver.title
        time.sleep(3)
        self.driver.find_element_by_css_selector("a.navbar-login").click()
        time.sleep(3)
        self.driver.find_element_by_id("user_phone").send_keys("13009433097")
        self.driver.find_element_by_id("user_pwd").send_keys("111111")
        self.driver.find_element_by_id("mulBtnSub").click()
        
#列表第一个大学，点击申请该学校按钮，再次点击申请该学校按钮；点击第二个大学对应申请该学校按钮
        self.driver.find_element_by_xpath(".//*[@id='show_list']/div[1]/div/div[3]/dl/dt/a[1]").click()
        self.driver.back()
        self.driver.find_element_by_xpath(".//*[@id='show_list']/div[1]/div/div[3]/dl/dt/a[1]").click()
        alert = self.driver.switch_to_alert()
        alert.accept()
        self.driver.find_element_by_xpath(".//*[@id='show_list']/div[2]/div/div[3]/dl/dt/a[1]").click()
        self.driver.back()
        self.driver.find_element_by_xpath(".//*[@id='show_list']/div[3]/div/div[3]/dl/dt/a[1]").click()
        self.driver.back()
        time.sleep(3)

        
    def tearDown(self):
        #self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()
    
       
if __name__ == "__main__": 
    unittest.main()
        
        
        