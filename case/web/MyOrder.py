from selenium import webdriver
from public.login import Mylogin
import unittest
import os
import time

class MyOrder(unittest.TestCase):

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

    def testysxt_012(self):
        '''验证无订单时默认文案是否正确'''
        Mylogin(self.driver).login()  # 登录
        self.driver.find_element_by_link_text('我的订单').click()
        time.sleep(2)
        cc=self.driver.find_element_by_xpath('//div[@class="nomsg"]/span')
        self.assertEqual("最近没有订单哦~", cc.text)  # 断言相等



    def testysxt_013(self):
        '''验证无退货维权订单时默认文案是否正确'''
        Mylogin(self.driver).login()  # 登录
        self.driver.find_element_by_link_text('我的订单').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('退货维权').click()
        time.sleep(3)
        dd=self.driver.find_element_by_xpath('//div[@class="nomsg"]/span')
        self.assertEqual("您还没有过退货维权哦~", dd.text)  # 断言相等


    def testysxt_014(self):
        '''验证无收货地址时默认文案是否正确'''
        Mylogin(self.driver).login()  # 登录
        self.driver.find_element_by_link_text('我的订单').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('收货地址').click()
        time.sleep(3)
        ee=self.driver.find_element_by_xpath('//div[@class="nomsg"]/span')
        self.assertEqual("您还没添加送货地址~", ee.text)  # 断言相等


    def testysxt_015(self):
        '''验证无关注时默认文案是否正确'''
        Mylogin(self.driver).login()  # 登录
        self.driver.find_element_by_link_text('我的订单').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('我的关注').click()
        time.sleep(3)
        ff=self.driver.find_element_by_xpath('//div[@class="nomsg"]/span')
        self.assertEqual("您还没有收藏产品~", ff.text)  # 断言相等



    def testysxt_016(self):
        '''验证无无交易时默认文案是否正确'''
        Mylogin(self.driver).login()  # 登录
        self.driver.find_element_by_link_text('我的订单').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('资金管理').click()
        time.sleep(3)
        gg = self.driver.find_element_by_xpath('//div[@class="nomsg"]/span')
        self.assertEqual("暂无交易", gg.text)  # 断言相等

    def testysxt_017(self):
        '''验证无无优惠券时默认文案是否正确'''
        Mylogin(self.driver).login()  # 登录
        self.driver.find_element_by_link_text('我的订单').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('资金管理').click()
        time.sleep(8)
        self.driver.find_element_by_link_text('提现管理').click()
        time.sleep(5)
        gh = self.driver.find_element_by_xpath('//div[@class="nomsg"]/span')
        self.assertEqual("您还没有提现过~", gh.text)  # 断言相等


    def testysxt_018(self):
        '''验证无无优惠券时默认文案是否正确'''
        Mylogin(self.driver).login()  # 登录
        self.driver.find_element_by_link_text('我的订单').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('我的优惠券').click()
        time.sleep(3)
        hh = self.driver.find_element_by_xpath('//div[@class="nomsg"]/span')
        self.assertEqual("还没有优惠券哦~", hh.text)  # 断言相等


    def testysxt_019(self):
        '''验证无通知时默认文案是否正确'''
        Mylogin(self.driver).login()  # 登录
        self.driver.find_element_by_link_text('我的订单').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('消息').click()
        time.sleep(3)
        ii = self.driver.find_element_by_xpath('//div[@class="nomsg"]')
        self.assertEqual("暂无消息", ii.text)  # 断言相等


    def testysxt_020(self):
        '''基本信息-验证是否可以更改个人信息'''
        Mylogin(self.driver).login()  # 登录
        self.driver.find_element_by_link_text('我的订单').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('账户设置').click()
        time.sleep(3)
        ai=self.driver.find_element_by_id('nick')
        aii=ai.send_keys('茉莉花')
        time.sleep(3)
        bi=self.driver.find_element_by_id('address')
        bii=bi.send_keys('湖南省')
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@class="submit"]').click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()   #弹框点击确认
        time.sleep(3)

        # 清空前面输入的内容
        self.driver.find_element_by_id('nick').clear()
        self.driver.find_element_by_id('nick').send_keys('清空')
        time.sleep(2)
        self.driver.find_element_by_id('address').clear()
        self.driver.find_element_by_id('address').send_keys('清空')
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@class="submit"]').click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()  # 弹框点击确认
        time.sleep(2)

        self.assertNotEqual("ai", aii)   #  断言不相等
        self.assertNotEqual("bi", bii)  # 断言不相等
        time.sleep(3)













if __name__ == "__main__":
    unittest.main()