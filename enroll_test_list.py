#coding=utf-8
#验证测试录取几率页面-PC列表页入口
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class enroll_list(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Firefox()
        self.verificationErrors = []
#打开院校库，用户登录        
    def test_enroll_list(self):
        u'''测试录取几率-pc端列表页'''
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

#断言 
         
        '''t1 = self.driver.find_element_by_xpath("//*[@id='user_title']/dt/a/span").text
        try:
            self.assertEqual(u'小晏晏啊非常',t1)

        except AssertionError as e:
            self.verificationErrors.append(str(e))
        #self.driver.find_element_by_xpath("//*[@id='example-navbar-collapse']/ul/li[2]/a").click()
        #print self.driver.title
       ''' 
       
#将滚动条移动到页面的底部        
        js="var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(3)
        
#点击列表页面测试录取几率        
        self.driver.find_element_by_xpath(".//*[@id='show_list']/div[9]/div/div[3]/dl/dt/a[2]").click()
        time.sleep(3)
        
#移动到新页面        
        allhandles=self.driver.window_handles
        for handle in allhandles:
            if handle != nowhandle:
                self.driver.switch_to_window(handle)
                print self.driver.title
                
        
#测试录取几率页面信息录入，提交后截图保存数据
        self.driver.find_element_by_xpath(".//*[@id='simCheck']/label[4]/span/i").click()
        self.driver.find_elements_by_xpath(".//*[@id='simSelect']/div/p/span")[0].click()
        time.sleep(3)
        self.driver.find_elements_by_xpath(".//*[@id='simSelect']/div/ul/li[3]/span")[0].click()
        time.sleep(3)
        self.driver.find_elements_by_xpath(".//*[@id='simSelect']/div/p/span")[1].click()
        time.sleep(5)
        self.driver.find_elements_by_xpath(".//*[@id='simSelect']/div/ul/li[4]/span")[1].click()
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='formFirst']/div[8]/span/input").send_keys("80")
        self.driver.find_elements_by_xpath(".//*[@id='simSelect']/div/p/span")[2].click()
        time.sleep(3)
        self.driver.find_elements_by_xpath(".//*[@id='simSelect']/div/ul/li[2]/span")[2].click()
        self.driver.find_element_by_xpath(".//*[@id='formFirst']/div[9]/span/input").send_keys("6.5")
        self.driver.find_element_by_xpath(".//*[@id='testBox']/label/i").click()
        self.driver.find_element_by_xpath(".//*[@id='nextId']").click()
        
        time.sleep(5)
        self.driver.save_screenshot('E:\\automation\\case_result\\case_screenshot\\result_listtest.png')
        #self.driver.execute_script("document.getElementsByClassName('comment-user')[0].click()")
        
#将滚动条移动到页面的顶部
        '''js_="var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js_)
        time.sleep(3)'''
    
  
    def tearDown(self):
        #self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()
    
       
if __name__ == "__main__": 
    unittest.main()