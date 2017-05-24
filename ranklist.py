#coding=utf-8
##验证院校库排行榜页面
from selenium import webdriver
import time
import unittest
from django.template.defaultfilters import title


class rank(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Firefox()
        self.verificationErrors = []

#打开院校库,根据学校名称进行查询-英国，输入学校关键字后进行查询，结果断言
    def test_rank(self):
        u'''基本查询功能用例'''
        self.driver.get('http://www.jiemo.net/School/Rank')
        self.driver.maximize_window()
        print self.driver.title
        '''self.driver.find_element_by_id("search_sh_name").send_keys(u"布里斯托大学")
        self.driver.find_element_by_xpath(".//*[@id='theform']/div[1]/div[1]/div/div[1]/div[2]/div/span/button").click()
        time.sleep(3)
        t1 = self.driver.find_element_by_xpath(".//*[@id='show_list']/div/div/div[2]/h3/a").text
        '''
        self.driver.implicitly_wait(60)
        
    
        links = self.driver.find_elements_by_tag_name("span")  
        for link in links:  
            if not "_blank" in link.get_attribute("target") and ("google" in link.get_attribute("href") or not "http" in link.get_attribute("href")):  
                link.click()
                self.driver.back()  

           
'''    def tearDown(self):
        self.driver.close()        
'''       
if __name__ == "__main__": 
    unittest.main()    