# javascript 是一门独立的语言
#要想学好selenium，最重要的三件事：
# 1.元素的定位：id--name -- class --link_text
#link_text定位方法的限制：必须是链接，即必须是<a>标签；必须是文本
# 2.元素的操作：鼠标左键单击click，发送键盘上的按键send_keys
# 3.学好javascript
# 用javascript实现窗口切换
#1.打开浏览器
from selenium import webdriver
import time
driver = webdriver.Chrome()
#driver.maximize_window()
driver.get("http://localhost")

#javascript和python是不同的语言，pycharm是用来写python语言的
#怎么在python执行javascript语言
js = 'document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js)

#2.点击登录链接
driver.find_element_by_link_text("登录").click()

# 输入用户名和密码
username_input = "#username"
driver.find_element_by_css_selector(username_input).send_keys("tzh1118")
#driver.find_element_by_id("username").send_keys("tzh")
driver.find_element_by_id("password").send_keys("123654")

# 点击登录按钮
driver.find_element_by_class_name("login_btn").click()
time.sleep(5)

# 点击返回商城的链接
store = "body > div.main.w1100 > div > div.content.fr > dl.dealing > dd > div > p > a"
driver.find_element_by_css_selector(store)

# 在搜索框中输入iphone，点击搜索按钮
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()

# 选择第一个商品点击查看详情
product_img = "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img"
driver.find_element_by_css_selector(product_img).click()

# 切换selenium工作窗口

cwh = driver.current_window_handle
whs = driver.window_handles
for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window(item)

# 加入购物车
driver.find_element_by_id("joinCarButton").click()

# 去购物结算
#driver.find_element_by_css_selector("body > div.shop_last.w1100 > div.other_shopl.fl > div.shopCar_T > span.shopCar_T_span2").is_displayed()
#driver.find_element_by_class_name("topCarBtn").click()
#driver.find_element_by_class_name("shopCar_T_span3").click()
#driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/span[2]").click()
time.sleep(10)
driver.execute_script('document.getElementsByClassName("shopCar_T")[0].childNodes[5].click()')

# 结算
driver.find_element_by_class_name("shopCar_btn_03").click()


#driver.quit()



