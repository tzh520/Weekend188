#1.打开浏览器
from selenium import webdriver
#从selenium导入网络驱动，用代码来操作浏览器的
#python语言不需要加分号
#Chrome后面一定要加括号，表示这是个方法
#修改字体步骤：File-->setting-->Editor-->color and font-->font-->修改字体大小
driver = webdriver.Chrome()
#2.打开注册页面
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
#3.输入用户名
driver.find_element_by_name("username").send_keys("tzh1118")
#4.输入密码
driver.find_element_by_name("password").send_keys("123654")
#5.输入确认密码
driver.find_element_by_name("userpassword2").send_keys("123654")
#6.输入手机号
driver.find_element_by_name("mobile_phone").send_keys("13645614725")
#7.输入邮箱
driver.find_element_by_name("email").send_keys("sweet@qq.com")
# 8.点击注册按钮
driver.find_element_by_class_name("reg_btn").click()

