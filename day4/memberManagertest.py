import unittest
# 1.导入ddt代码库
import ddt

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day4.readCsv2 import read

# 2.装饰这个类
@ddt.ddt
class MemberManagerTest(unittest.TestCase):
    # 3.调用之前写好的read()方法，获取配置文件的数据
    member_info = read("member_info.csv")
    # global driver
    # 在当前类只执行一次
    @classmethod
    def setUpClass(cls):
        print("所有方法之前，执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        # cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        print("所有方法执行之后，执行一次")
        time.sleep(20)
        cls.driver.close()

# unittest中测试方法按照字母顺序执行
    def test_a_log_in(self):
        print("登录测试")
        driver = self.driver
        driver.get("http://localhost/admin.php")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234")  .send_keys(Keys.ENTER).perform()
        # driver.find_element_by_name("userpass").send_keys("password")

    # python中集合或列表前面的星号，表示把集合中的所有元素拆开，一个一个写
    # 如，list = ["小红"，"小黑"]
    # *list = "小红"，"小黑"
    # 星号的作用是把一个列表拆成多个String
    # 假如，一个方法需要接收两个参数，肯定不能传一个list进去
    # 但是如果list中正好也是两个元素，这时在列表前面加一个星号，
    # 这时就不再认为是一个列表了，可以视为两个参数
    # 5.@ddt.data() 测试数据来源于read()方法
    # 5.把数据表中的每一行传入方法，在方法中增加一个参数row
    @ddt.data(*member_info)
    def test_b_add_member(self, row):
        # print("添加会员")
        driver = self.driver
        # 每组测试数据就是一条测试用例，每条测试用例是独立的，不能因为上一条测试用例执行失败（断言失败），导致下一组数据不能被正常执行，所以这里不推荐用for循环，
        # 应该用ddt装饰器，去修饰这个方法，达到测试用例每条独立执行的目的
        # ddt 数据驱动测试 data driver test
        # 4.注释掉for循环，改变代码的缩进(shift+tab快捷键)，使方法中的代码比方法声明缩进4个空格
        # for row in read("member_info.csv"):
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        # driver.switch_to.frame("mainframe")
        # 如果frame没有name属性时，我们可通过其他方式定位iframe标签，把定位好的页面元素传给driver.switch_to.frame()方法也可以实现frame切换
        iframe_css = "#mainFrame"
        iframe_html = driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        time.sleep(2)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        # '[value='"+row[2]+"'] '== '[value="1"]'
        # "[value='{0}']".format(row[2])
        # driver.find_element_by_css_selector("[name='sex'][value='"+row[2]+"']").click()
        driver.find_element_by_css_selector("[value='{0}']".format(row[2])).click()

        driver.find_element_by_name("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()
        # print("value="+row[2]+"1")
        # print('[value='"+row[2]+"']')

        # 之前的代码是能够自动运行，但是还不能自动判断程序运行的是否正确
        # 我们自动化代码不能找人一直盯着运行，检查是否执行正确
        # actual 实际结果，执行测试用例之后，页面上实际显示的结果
        # 获取元素的文本
        time.sleep(2)
        actual = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        # datagrid-row-r1-2-0 > td:nth-child(1) > div
        # expected 期望结果，来自于手动测试用例或者需求文档，配置文件
        expected = row[0]
        # 断言类似与if...else...语句，是用来做判断的
        # if actual == expected:
        #     print("测试通过")
        # else:
        #     print("测试失败")

        # 切换到父框架
        # driver.switch_to.parent_frame()
        # 切换到网页的根节点
        driver.switch_to.default_content()
        # 断言叫assert，断言是框架提供的，要想调用断言，必须要加上self.，因为测试用例类继承了框架中的TestCase类，也继承了这个类中的断言，所以我们可以直接用断言方法
        # 断言有几个特点：
        # 1.断言更简洁
        # 2.断言关注于错误的测试用例，只有断言结果出错时，才会打印信息，正确时没有任何信息提示
        # 3.断言报错时，后面的代码将不会继续执行，前面的步骤失败了，后面的步骤就不需要继续尝试了，提高性能
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()


