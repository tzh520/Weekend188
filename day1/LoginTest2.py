#1.打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://172.31.6.64/")

#2.点击登录链接
driver.find_element_by_link_text("登录").click()

#   从浏览器中所有窗口中排除第一个，剩下第二个窗口，把selenium切换到第二个窗口
#获取第一个页面的句柄
cwh = driver.current_window_handle
whs = driver.window_handles
for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window(item)



#3.输入用户名，密码
driver.find_element_by_id("username").send_keys("tzh")
driver.find_element_by_id("password").send_keys("123456")

#4.点击登录按钮
driver.find_element_by_class_name("login_btn").click()