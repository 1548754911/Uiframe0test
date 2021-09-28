# coding=utf-8
from selenium import webdriver
from public.login import Mylogin
import unittest
import os
import time

class TestShouye(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://101.133.169.100/yuns/index.php")
        self.driver.maximize_window()
        time.sleep(5)
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    def testysxt_001 (self):
        '''测试首页导航文案显示是否正常'''
        Mylogin(self.driver).login()
        firstPageNavi = self.driver.find_element_by_xpath("//div[@class='top']/span")
        loginText = self.driver.find_element_by_css_selector("div.login>a:nth-child(1)")
        regisText = self.driver.find_element_by_css_selector("div.login>a:nth-child(3)")

        self.assertEqual("亲，欢迎您来到云商系统商城！",firstPageNavi.text)    #断言相等，
        self.assertEqual("清空", loginText.text)
        self.assertEqual("退出", regisText.text)

        #断言的方法
        # self.assertNotEqual("dd", regisText.text)        #断言不相等，可用于以下场景：1、删除信息，进行检查
        #
        # self.assertIn("云商系统商城",firstPageNavi.text)    #断言前面的内容是否被后面包含
        # self.assertNotIn("云商系统商城",firstPageNavi.text)    #前面的内容不被后面包含
        #
        # self.assertTrue(self.driver.find_element_by_xpath("//div[@class='top']/span").is_displayed())  #判断括号里面的内容是True还是False,返回true执行成功，返回false失败
        #                                                                                                    #多用于判断页面是否加载出来
        # self.assertFalse(firstPageNavi.is_displayed())
        # #万能的断言方式，
        # if loginText.text == "177****0979":
        #     print("等于")
        # else:
        #     print("不等于")
        #     self.driver.find_element_by_xpath("王麻子")

    def testysxt_002(self):
       ''' 验证搜索出正确结果是否正确'''
       Mylogin(self.driver).login()
       self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys("女装")
       self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[2]").click()
       time.sleep(3)
       chaxun=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[1]/div[3]/div[2]/a')
       self.assertIn("女装", chaxun.text)



    def testysxt_003(self):
        '''验证搜索内容无时，提示语是否正常'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys("王麻子")
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[2]").click()
        time.sleep(2)
        searchText = self.driver.find_element_by_xpath("//div[@class='nomsg']")
        self.assertEqual(searchText.text, "抱歉，没有找到相关的商品")



    def testysxt_021(self):
        '''验证点击‘免费注册’能否跳转到注册页面'''
        self.driver.find_element_by_link_text('免费注册').click()

        register=self.driver.find_element_by_xpath('//div[@class="reg_bname"]/span')
        self.assertEqual("用户注册", register.text)  # 断言相等


    def testysxt_022(self):
        ''' 验证退出功能'''
        Mylogin(self.driver).login()
        out1=self.driver.find_element_by_link_text('退出')
        out2=self.driver.find_element_by_link_text('退出').click()
        time.sleep(3)
        self.assertNotEqual("out1", out2)   #断言不相等

    def testysxt_023(self):
        '''  验证会员中心功能'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_link_text('会员中心').click()
        time.sleep(3)
        member=self.driver.find_element_by_xpath('//div[@class="left"]/strong')

        self.assertEqual("会员中心", member.text)  # 断言相等


    def testysxt_024(self):
        '''  验证联系客服功能'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_link_text('联系客服').click()
        time.sleep(3)
        member1=self.driver.find_element_by_xpath('//div[@class="nm"]/span')


        self.assertEqual("联系我们", member1.text)  # 断言相等

    def testysxt_025(self):
            '''  验证首页控件'''
            Mylogin(self.driver).login()
            self.driver.find_element_by_link_text('会员中心').click()
            time.sleep(3)
            self.driver.find_element_by_link_text('首页').click()
            time.sleep(5)
            aaa=self.driver.find_element_by_link_text('联系客服')

            self.assertEqual("联系客服", aaa.text)  # 断言相等

















if __name__ == "__main__":      #类的执行入口，是python类的入口函数
    unittest.main()


