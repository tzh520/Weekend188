#有了MyTestCase以后，再写测试用例就不需要重新写setUp和tearDown方法了
import os

from selenium import webdriver
from day5.myTestCase import MyTestCase


# 因为MyTestCase已经实现了setUp和tearDown方法，我们以后再写测试用例，就不需要重新实现这两个方法了
# 可以直接继承MyTestCase,不需要再继承Unittest.TestCase了，因为MyTestCase继承了Unittest.TestCase，继承是可传递的
class SignInTest(MyTestCase):
    # 三个双引号表示文档字符串，也是一种注释，和#的区别是，这种注释会显示在文档中
    """海盗商城注册模块测试用例"""

    def test_signin(self):
        """打开注册页面的测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        # 使用网址写断言，判断是否成功打开网址
        print(driver.current_url) # 用来获取当前浏览器中的网址
        actual = driver.title  # 用来获取当前浏览器中的标签页的title
        expected = "用户注册 - 道e坊商城 - Powered by Haidao11"
        # get_screenshot_as_file(self, filename) 截取整个浏览器的图片
        base_path = os.path.dirname(__file__)
        path = base_path.replace("day5","report/image/")
        # 如果报chrome 62……版本，是因为浏览器和浏览器驱动不匹配，需要重新安装版本匹配的浏览器和浏览器驱动
        driver.get_screenshot_as_file(path + "signin.png")
        self.assertEqual(actual,expected)
