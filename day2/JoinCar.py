# 打开浏览器
import time
from selenium import webdriver


# 45版本以下的FireFox浏览器不需要驱动文件
# 46版本开始的firefox浏览器，也需要把驱动文件（driver.exe）放在环境变量下
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Ie()
# 隐式等待一经设置，对后面的所有语句都有效果，所以只要在创建浏览器时设置一次就可以了
# implicitly 含蓄的，委婉的
driver.implicitly_wait(30)
#driver.maximize_window()

driver.get("http://localhost/")
# 在点击登录按钮之前，我们需要先删除target属性
# 但是javascript定位方式比selenium麻烦
# 可不可以用selenium的定位方式来替换javascript的定位方式呢？
# 用arguments关键字，可以把元素定位作为一个参数，替换到javascript语句中
login_link = driver.find_element_by_link_text("登录")
# 使用login_link这个定位方式来删除target这个属性
# arguments[0]表示逗号后面的第一个参数，
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
driver.find_element_by_id("username").send_keys("tzh1118")
driver.find_element_by_id("password").send_keys("123654")
driver.find_element_by_id("password").submit()
# submit()方法是用于提交form表单的，form是html中的一个元素
# form表单中的任何子孙节点都可以调用submit()方法提交表单
# submit()方法只适用于form表单，它只是调用html中的方法，没有模拟鼠标的操作，所以尽量不要用
# Alt + Enter 可以自动导包
# time.sleep(5)
# time.sleep到底设成几秒好？几秒都不好
# 应该使用隐式等待（智能等待），会自动判断网页是否加载完毕，当加载完毕立刻开始下面操作
# 要设置一个最大时间，不能让程序无限等待，一般这个时间是30秒

driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#iphone_img = "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img"

iphone_link = "div.shop_01-imgbox > a"
iphone = driver.find_element_by_css_selector(iphone_link)
# div.shop_01-imgbox：div表示节点名字，点表示class
# img是标签名，>标签表示前面的是父节点，后面的是子节点+/-
# 如果要在css中写class，那么前面需要加上点
# :nth-child(2)表示当前节点在家中排行老二，是它父亲的第二个儿子
# 为什么要把css selector中的内容改的越短越好？
# 涉及到越多的网页元素（节点），代码的健壮性和可维护性就越差
# 因为开发一旦修改页面时，修改了这些节点，那么元素就会定位失败
driver.execute_script("arguments[0].removeAttribute('target')",iphone_link)
iphone_link.click()
# arguments[0].removeAttribute('target')

# 点击加入购物车按钮
time.sleep(5)
driver.find_element_by_id("joinCarButton").click()

driver.find_element_by_class_name("shopCar_T_span3").click()

driver.find_element_by_link_text("结算").click()

driver.find_element_by_class_name("add-address").click()

#driver.switch_to().alert().accept()
# 填写收货人
driver.find_element_by_name("address[address_name]").send_keys("tzh")
# 填写手机号
driver.find_element_by_name("address[mobile]").send_keys("15698741258")
# 下拉框选择
# driver.find_element_by_id("add-new-area-select").find_element_by_css_selector("#add-new-area-select > option:nth-child(9)")
# driver.find_element_by_css_selector('[value="230000"]').click()
# driver.find_element_by_id("add-new-area-select").find_element_by_css_selector('[value="230000"]').click()
sheng = driver.find_element_by_id("add-new-area-select")
# print(type(sheng)) 打印变量类型
# 下拉框是一种比较特殊的网页元素，selenium专门为下拉框提供了一种定位方式
# 把下拉框元素从 WebElement 类型转换成 select 类型
# Select是selenium专门为我们创建的一个类，用于操作下拉框的
# Select这个类中封装了很多操作下拉框的方法
Select(sheng).select_by_value('230000')
# driver.find_element_by_css_selector('[value="230500"]')
# shi = driver.find_element_by_xpath('//*[@id="add-new-area-select"]')
# Select(shi).deselect_by_value("230500")
# 定位第二个下拉框
shi = driver.find_elements_by_tag_name("select")[1]
Select(shi).select_by_index(2)

# driver.find_element_by_css_selector('[value="230506"]')
qu = driver.find_elements_by_tag_name("select")[2]
Select(qu).select_by_visible_text("碾子山区")
# qu = driver.find_element_by_id("linkagesel_480893")
# Select(qu).deselect_by_value("230506")


driver.find_element_by_name("address[address]").send_keys("灯影胡同20号")
driver.find_element_by_name("address[zipcode]").send_keys("653214")

driver.find_element_by_class_name("aui_state_highlight").click()


#driver.switch_to().alert().dismiss()














