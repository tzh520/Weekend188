import unittest

import time
from selenium import webdriver

class MemberManageTest(unittest.TestCase):
    # 变量前面加上self.表示这个变量是类的属性，可以被其他方法调用
    def setUp(self):
        # 打开浏览器
        # driver声明在setUp方法之内，不能被其他方法访问
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # driver.maximize_window()

    def tearDown(self):
        # quit()退出整个浏览器
        # close()关闭一个浏览器标签
        # 代码编写和调试的时候需要在quit()方法前加一个时间等待，方便看清楚执行过程
        # 正式运行时，去掉时间等待，可以提高程序执行速度
        time.sleep(20)
        self.driver.quit()

    def test_add_member(self):
        driver = self.driver
        driver.get("http://localhost/index.php?&m=admin&c=public&a=login")

        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_class_name("Btn").click()

        time.sleep(2)
        driver.find_element_by_link_text("会员管理").click()

        time.sleep(2)
        driver.switch_to.frame("mainFrame")
        time.sleep(2)

        driver.find_element_by_css_selector("#addrow > span").click()
        time.sleep(2)

        driver.find_element_by_name("username").send_keys("tzh11")
        driver.find_element_by_name("mobile_phone").send_keys("13645678933")
        driver.find_element_by_css_selector('body > div.content > div.install.mt10 > dl > dd > div > div > dl > form > dd > ul > li:nth-child(3) > b > label:nth-child(2) > input[type="radio"]').click()
        driver.find_element_by_id("birthday").send_keys("2000-05-02")
        driver.find_element_by_name("email").send_keys("123@qq.com")
        driver.find_element_by_name("qq").send_keys("1478569321")
        driver.find_element_by_class_name("button_search").click()




