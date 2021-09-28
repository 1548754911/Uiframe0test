import time
class Mylogin(object):
    def __init__(self, driver):
        self.driver = driver
        '''登录'''
    def login(self):
        self.driver.find_element_by_link_text("登录").click()
        time.sleep(2)
        self.driver.find_element_by_name("username").send_keys("3233613369@qq.com")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_class_name("submit_login").click()
        time.sleep(3)

    '''添加一件商品到购物车'''
    def shopping(self):
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/input[1]").send_keys('女装')  # 点击搜索框
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[2]').click()
        time.sleep(3)
        # dianji=self.driver.find_element_by_link_text('毛衣女装').click()  # 点击女装
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[1]/div[1]/a').click()  # 点击女装
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])  # 句柄切换
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[1]/dd/a[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[2]/dd/a[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[3]/dd/a[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[4]/div[2]/a[1]').click()  # 加入购物车
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/div/div[2]/a[1]').click()  # 进入购物车
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])  # 句柄切换





        # self.driver.find_element_by_xpath('').click()

    