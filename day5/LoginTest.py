import unittest

import time
from selenium import webdriver


class LoginTest(unittest.TestCase):
    """海盗商城登录模块测试用例"""
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        print("setUp")
        self.driver.implicitly_wait(30)
        #浏览器的版本和driver的版本必须匹配才能用窗口最大化
        #driver.maximize_window()

    def tearDown(self):
        time.sleep(2)
        print("tearDown")
        self.driver.quit()

    def test_Login(self):
        """登录模块正常情况测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("tzh1118")
        driver.find_element_by_id("password").send_keys("123654")
        driver.find_element_by_class_name("login_btn").click()
        print("当前用户名：tzh1118")




