from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        # 构造方法的作用：实例化LoginPage对象的时候，必须要调用构造方法
        # python中构造方法是固定写法，__inti__表示 构造方法 intimate
        # 需要把driver作为参数传进来
        #方便别的属性和方法使用driver
        self.driver = driver
    # 固定的东西不需要卸载构造方法中，构造方法只写变化的东西
    title = "用户登录 - 道e坊商城 - Powered by Haidao"
    url = "http://localhost/index.php?m=user&c=public&a=login"


    # 用一个元组（小括号）描述的元素，元组中有两个元素，第一个元素是控件的定位方式，第二个元素是控件定位方式的具体值
    # 下面两个都是类的成员变量
    username_input_local = (By.ID, "username")
    passname_input_local = (By.ID, "password")
    login_button_local = (By.CLASS_NAME, "login_btn")

    def open(self):
        self.driver.get(self.url)

    def input_username(self, username):
        # self.driver.find_element_by_id("username").send_keys(username)
        # 星号的作用就是把一个元组中的元素分别传入方法参数中
        # 前面加一个星号，表示传入就不是元组，而是元组中的两个元素
        self.driver.find_element(*self.username_input_local).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.passname_input_local).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_local).click()


