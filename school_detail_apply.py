#coding=utf-8
#申请该学校-PC详情页
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class school_detail_apply(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Firefox()
        self.verificationErrors = []

#  打开院校库，用户登录              
    def test_school_detail_apply(self):
        u'''申请该学校-pc端详情页'''
        self.driver.get('http://www.jiemodou.net/school')
        self.driver.maximize_window()
        nowhandle=self.driver.current_window_handle
        time.sleep(3)
        self.driver.find_element_by_css_selector("a.navbar-login").click()
        time.sleep(3)
        self.driver.find_element_by_id("user_phone").send_keys("13009433097")
        self.driver.find_element_by_id("user_pwd").send_keys("111111")
        self.driver.find_element_by_id("mulBtnSub").click()
        
        self.driver.find_element_by_xpath(".//*[@id='show_list']/div[4]/div/div[2]/h3/a").click()
        
#移动到新详情页面-第一所学校 ，关闭当前页面返回上级页面   ，点击第二所学校 
        allhandles=self.driver.window_handles
        for handle in allhandles:
            if handle != nowhandle:
                self.driver.switch_to_window(handle)
               
                
        self.driver.find_element_by_xpath(".//*[@id='collegeBasic']/div/div[2]/div/div[3]/dl/dt/a[1]").click()
        self.driver.close()
        self.driver.switch_to_window(nowhandle)
        self.driver.find_element_by_xpath(".//*[@id='show_list']/div[5]/div/div[2]/h3/a").click()
        
#移动到新详情页面 -第二所学校     ，关闭当前页面返回上级页面   ，点击第三所学校        
        allhandles=self.driver.window_handles
        for handle in allhandles:
            if handle != nowhandle:
                self.driver.switch_to_window(handle)
                
        self.driver.find_element_by_xpath(".//*[@id='collegeBasic']/div/div[2]/div/div[3]/dl/dt/a[1]").click()
        self.driver.close()
        self.driver.switch_to_window(nowhandle)
        self.driver.find_element_by_xpath(".//*[@id='show_list']/div[6]/div/div[2]/h3/a").click()

#移动到新详情页面 -第二所学校     ，关闭当前页面返回上级页面   ，点击第三所学校        
        allhandles=self.driver.window_handles
        for handle in allhandles:
            if handle != nowhandle:
                self.driver.switch_to_window(handle)
        self.driver.find_element_by_xpath(".//*[@id='collegeBasic']/div/div[2]/div/div[3]/dl/dt/a[1]").click()


#弹出选择学校已达上限alert，点击确定       
        alert = self.driver.switch_to_alert()
        alert.accept()  
        

     
    def tearDown(self):
        #self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()           
                
        
        
        
if __name__ == "__main__": 
    unittest.main()      
        