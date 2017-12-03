# 1.登录
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()

# 2.商品管理
driver.find_element_by_link_text("商品管理").click()
time.sleep(5)

# 3.添加商品
driver.find_element_by_link_text("添加商品").click()
# 有一种特殊的网页，比如左边或者上边有一个导航条，这时要注意了
# 开发喜欢在一个页面中嵌套多个页面
# 其中商品管理和添加商品属于页面根节点的网页
# 商品名称属于frame框架里的子网页
# 之前讲过窗口切换，用于不用网页之间的页面切换
# 有网页嵌套也需要切换网页
driver.switch_to.frame("mainFrame")

# 4.商品名称
driver.find_element_by_name("name").send_keys("iphone 8")

# 5.商品分类
driver.find_element_by_css_selector("[id='1']").click()
driver.find_element_by_xpath('//*[@id="2"]').click()
driver.find_element_by_id("6").click()
iphone = driver.find_element_by_id("7")

# 双击是特殊的元素操作，所有的特殊操作被封装到ActionChains这个类中，chain链条，类似与数组的东西
# driver封装到Actions这个类中
# 链表必须以perform方法为结尾

ActionChains(driver).double_click(iphone).perform()
# 组合点击
# ActionChains(driver).click(driver.find_element_by_id("6")).double_click(iphone).perform()

# 6.商品品牌
brand = driver.find_element_by_name("brand_id")
Select(brand).select_by_index(1)
time.sleep(5)

# 7.点击提交
brand.submit()