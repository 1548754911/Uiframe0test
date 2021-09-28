# coding=utf-8
from selenium import webdriver
import unittest
import os
import time
from public.login import Mylogin

class Gouwuche(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://101.133.169.100/yuns/index.php")
        self.driver.maximize_window()
        time.sleep(5)

    def tearDown(self):
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    def testysxt_004(self):
        '''购物车为空时文案显示是否正常'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//div[@class='small_cart_name']/span").click()
        time.sleep(3)
        emptyGouwuText = self.driver.find_element_by_xpath("//div[@class='r']/span")
        print(emptyGouwuText.text)
        self.assertEqual("购物车内暂时没有商品",emptyGouwuText.text)

    def testysxt_005(self):
        '''验证“现在就去购物”功能是否能使用'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//div[@class='small_cart_name']/span").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div/div/div/div[2]/a").click()   #点击“现在就去购物”功能
        time.sleep(5)
        shouye = self.driver.find_element_by_xpath("//div[@class='top']/span")
        self.assertEqual("亲，欢迎您来到云商系统商城！",shouye.text)       #断言相等，

    def testysxt_006(self):
        '''验证添加到购物车的商品是否一致'''
        Mylogin(self.driver).login()  #登录
        # self.driver.find_element_by_link_text('女装').click()
        # self.driver.find_element_by_link_text('毛衣女装').click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/input[1]").send_keys('女装')   # 点击搜索框
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[2]').click()
        time.sleep(3)
        # dianji=self.driver.find_element_by_link_text('毛衣女装').click()  # 点击女装
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[1]/div[1]/a').click()  # 点击女装
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])  #句柄切换
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[1]/dd/a[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[2]/dd/a[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[3]/dd/a[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[4]/div[2]/a[1]').click()  # 加入购物车
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/div/div[2]/a[1]').click()  # 进入购物车
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])  # 句柄切换
        jia=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/a')
        self.assertEqual("毛衣女装",jia.text)       #断言相等

    def testysxt_007(self):
        '''验证数量增加功能是否正常'''
        Mylogin(self.driver).login()  #登录
        Mylogin(self.driver).shopping()  # 添加一件商品到购物车
        quantity1=self.driver.find_element_by_xpath('//div[@id="total_num"]/span')
        time.sleep(2)
        self.driver.find_element_by_link_text('+').click()
        time.sleep(2)
        quantity2 = self.driver.find_element_by_xpath('//div[@id="total_num"]/span')
        self.assertNotEqual("quantity1", quantity2.text)  # 断言不相等

    def testysxt_008(self):
        '''验证数量减少功能是否正常'''
        Mylogin(self.driver).login()  #登录
        Mylogin(self.driver).shopping()  # 添加一件商品到购物车
        self.driver.find_element_by_link_text('+').click()   #增加一件商品
        time.sleep(2)
        reduce1=self.driver.find_element_by_xpath('//div[@id="total_num"]/span')  #增加后获取有几件
        time.sleep(2)
        self.driver.find_element_by_link_text('-').click()  # 减少一件商品
        time.sleep(2)
        reduce2= self.driver.find_element_by_xpath('//div[@id="total_num"]/span')  #减少后获取有几件
        self.assertNotEqual("reduce1", reduce2.text)  # 断言不相等

    def testysxt_009(self):
        '''验证删除功能是否正常'''
        Mylogin(self.driver).login()  #登录
        Mylogin(self.driver).shopping()  # 添加一件商品到购物车
        self.driver.find_element_by_link_text('删除').click()
        time.sleep(5)
        delete=self.driver.find_element_by_xpath('//div[@class="r"]/span')
        time.sleep(5)
        self.assertEqual("购物车内暂时没有商品", delete.text)       # 断言相等

    def testysxt_010(self):
        '''验证去结算功能是否正常'''
        Mylogin(self.driver).login()  # 登录
        Mylogin(self.driver).shopping()  # 添加一件商品到购物车
        payment1=self.driver.find_element_by_xpath('//input[@class="gopay"]').click()
        time.sleep(3)
        payment2=self.driver.find_element_by_xpath('//input[@class="gopay"and@value="下单支付"]')
        time.sleep(3)
        self.assertNotEqual("payment1",payment2.text)  # 断言不相等

    def testysxt_011(self):
        '''验证勾选功能是否正常'''
        Mylogin(self.driver).login()  # 登录
        Mylogin(self.driver).shopping()  # 添加一件商品到购物车
        click1=self.driver.find_element_by_xpath('//div[@id="total_num"]/span')
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@name="cartid[]"]').click()
        time.sleep(2)
        click2 = self.driver.find_element_by_xpath('//div[@id="total_num"]/span')
        time.sleep(2)
        self.assertNotEqual("click1", click2.text)    # 断言不相等



if __name__ == "__main__":
    unittest.main()


