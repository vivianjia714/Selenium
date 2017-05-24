#coding=utf-8
##验证测试录取几率页面-PC详情页入口
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class enroll_detail(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Firefox()
        self.verificationErrors = []
#打开院校库，用户登录        
    def test_enroll_detail(self):
        u'''测试录取几率-pc端详情页'''
        self.driver.get('http://www.jiemodou.net/school')
        self.driver.maximize_window()
        nowhandle=self.driver.current_window_handle
        print self.driver.title
        time.sleep(3)
        self.driver.find_element_by_css_selector("a.navbar-login").click()
        time.sleep(3)
        self.driver.find_element_by_id("user_phone").send_keys("13009433097")
        self.driver.find_element_by_id("user_pwd").send_keys("111111")
        self.driver.find_element_by_id("mulBtnSub").click()
        
        
#将滚动条移动到页面的底部        
        js="var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(3)
        
#点击跳转到第N页
        self.driver.find_element_by_xpath(".//*[@id='theform']/ul/div/ul/li[3]/a").click()
        self.driver.find_element_by_xpath(".//*[@id='show_list']/div[1]/div/div[2]/h3/a").click()
                
#点击学校名称移动到学校详情页面        
        allhandles=self.driver.window_handles
        for handle in allhandles:
            if handle != nowhandle:
                self.driver.switch_to_window(handle)
                print self.driver.title
                
        self.driver.find_element_by_xpath(".//*[@id='pi_t']/a").click()
        time.sleep(3)    
        self.driver.find_element_by_xpath(".//*[@id='zhuanye_list']/div[1]/dl[3]/dd/p/a[1]").click()


#测试录取几率页面信息录入，提交后截图保存数据
        self.driver.find_element_by_xpath(".//*[@id='simCheck']/label[2]/span/i").click()
        self.driver.find_elements_by_xpath(".//*[@id='simSelect']/div/p/span")[0].click()
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='simSelect']/div/ul/li[5]/span").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='formFirst']/div[8]/span/input").send_keys("80")
        self.driver.find_elements_by_xpath(".//*[@id='simSelect']/div/p/span")[2].click()
        time.sleep(3)
        self.driver.find_elements_by_xpath(".//*[@id='simSelect']/div/ul/li[2]/span")[2].click()
        self.driver.find_element_by_xpath(".//*[@id='formFirst']/div[9]/span/input").send_keys("6.5")
        self.driver.find_element_by_xpath(".//*[@id='testBox']/label/i").click()
        self.driver.find_element_by_xpath(".//*[@id='nextId']").click()      
        time.sleep(5)
        self.driver.save_screenshot('E:\\automation\\case_result\\case_screenshot\\result_testdetail.png')

                   
    def tearDown(self):
        #self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()
    
       
if __name__ == "__main__": 
    unittest.main()        
        
