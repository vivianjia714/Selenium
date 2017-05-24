#coding=utf-8
##验证申请该专业页面-PC列表页入口
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class major_apply(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Firefox()
        self.verificationErrors = []
#打开院校库，用户登录        
    def test_major_apply(self):
        u'''申请专业'''
        self.driver.get('http://www.jiemodou.net/school')
        self.driver.maximize_window()
        nowhandle=self.driver.current_window_handle
        print self.driver.title
        time.sleep(3)
        self.driver.find_element_by_css_selector("a.navbar-login").click()
        time.sleep(3)
        self.driver.find_element_by_id("user_phone").send_keys("13009432667")
        self.driver.find_element_by_id("user_pwd").send_keys("111111")
        self.driver.find_element_by_id("mulBtnSub").click()

#点击学校名称 -伦敦大学学院       
        self.driver.find_element_by_xpath(".//*[@id='show_list']/div[10]/div/div[2]/h3/a").click()
        
#移动到新页面        
        allhandles=self.driver.window_handles
        for handle in allhandles:
            if handle != nowhandle:
                self.driver.switch_to_window(handle)
                print self.driver.title
        
        self.driver.find_element_by_xpath(".//*[@id='pi_t']/a").click()
        time.sleep(3)
        
#点击申请该专业        
        self.driver.find_element_by_xpath(".//*[@id='zhuanye_list']/div[1]/dl[4]/dd/p/a[2]").click()
        print self.driver.title
        self.driver.back()
        time.sleep(3)
       
        self.driver.find_element_by_xpath(".//*[@id='zhuanye_list']/div[1]/dl[5]/dd/p/a[2]").click()
        print self.driver.title
        self.driver.back()
        time.sleep(3)
        
#申请大于两个专业后，点击确定接受alert        
        self.driver.find_element_by_xpath(".//*[@id='zhuanye_list']/div[1]/dl[6]/dd/p/a[2]").click()
        alert = self.driver.switch_to_alert()
        alert.accept()
        

          
    def tearDown(self):
        #self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()
    
       
if __name__ == "__main__": 
    unittest.main()