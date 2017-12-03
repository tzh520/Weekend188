import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.page_object.loginPage import LoginPage
from day6.page_object.personalCenterPage import PersonalCenterPage


class LoginTest(MyTestCase):
    def test_login(self):
        # 现在这种测试用例可读性比较差，维护起来比较困难
        #那么测试用例写成什么样可读性比较好呢
        driver = self.driver
        # 1.打开网页
        # driver.get("http://localhost/index.php?m=user&c=public&a=login")
        lp = LoginPage(driver) # 实例化一个登录页面
        lp.open()  # 打开登录页面

        # 2.输入用户名
        # driver.find_element_by_id("username")
        #driver.find_element(By.ID, "username").send_keys("tzh1118")
        lp.input_username("tzh1118")

        # 3.输入密码
        # driver.find_element(By.ID, "password").send_keys("123654")
        lp.input_password("123654")

        # 4.点击登录按钮
        # driver.find_element(By.CLASS_NAME, "login_btn").click()
        lp.click_login_button()

        # 5.验证是否跳转到管理中心页面
        # expected = "我的会员中心 - 道e坊商城 - Powered by Haidao"
        # self.assertIn("我的会员中心", driver.title)
        pcp = PersonalCenterPage(driver)
        time.sleep(3)
        self.assertEqual(pcp.title, driver.title)



