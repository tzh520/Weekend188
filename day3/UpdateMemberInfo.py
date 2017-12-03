# 1.登录
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("tzh1118")
# 使用tab键切换输入框，使用Keys()方法找到想要输入的键
#driver.find_element_by_id("username").send_keys(Keys.TAB)  对username输入tab键
# 对driver（整个浏览器）输入tab键
# Chain链表和数组不同，数组有固定的长度，链表必须有明确的结束标志.perform()
ActionChains(driver).send_keys(Keys.TAB).send_keys("123654").send_keys(Keys.ENTER).perform()


# 2.点击账号设置
driver.find_element_by_link_text("账号设置").click()
time.sleep(5)

# 3.点击个人资料
# 使用partial_link定位比较好，因为在link中间除了“个人资料”还有别的信息

driver.find_element_by_partial_link_text("个人资料").click()

# 4.修改个人信息
# clear 清空的意思，用来清空元素中原本的内容
# 更好的编程习惯是，在每次执行send_keys之前都进行clear操作
# 4a.真实姓名
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("田田")
# 4b.性别
# "#xb[value='2']"是组合定位，#xb和[value='2']中间不能有空格，空格表示子孙节点
# css可以用多个属性组合定位一个元素
# 一个元素的多个属性之间不能有空格
driver.find_element_by_css_selector("#xb[value='2']").click()

# 4c.生日
# 将只读readonly属性删除掉，然后手动输入
# javascript是一个单独的语言，和python语法不一样，不能直接在pycharm中执行
# js = 'document.getElementById("date").removeAttribute("readonly")'
# driver.execute_script(js)
# driver.find_element_by_id("date").send_keys("1990-05-02")
# 用arguments改写上面的输入
# 使用selenium的定位方式代替javascript定位方式，driver.find_element_by_id("date")--document.getElementById("date")
# 用selenium定位方式定位元素之后，对元素执行javascript脚本，删除readonly属性
# "ctrl+/" 解除注释快捷键
date = driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")', date)
date.clear()
date.send_keys("1990-05-02")

# 用selenium调用javascript一共有两个关键字：
# 1.arguments[0]：表示用python语言代替一部分javascript
# 好处是，有时selenium定位比较容易
# 2.return 返回值，把javascript执行结果返回给python语言
# 好处是，有时selenium定位不到的元素（通过javascript动态生成的元素不容易定位到），可以用javascript定位到

# date = driver.execute_script("return document.getElementById('date')")
# 上面这句话==date = driver.find_element_by_id("date")
# date.click()
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("52879655")
driver.find_element_by_class_name("btn4").click()

# 右键检查不了的html代码的弹出框，叫alert，有单独的处理方法
time.sleep(3)
# alert控件不是html代码生成的，所以implicitly_wait对这个控件不管用
# 所以就算上面写了implicitly_wait，这个time_sleep()方法不能省略
# 切换到alert的方法，和切换窗口的方法类似
# alert 弹出框，accept 接受\同意\确定，dismiss 拒绝\取消
driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()


# arg1 = a.get_attribute('value')
# if arg1 != "1987-05-02":
#    a.click()

# driver.find_element_by_css_selector("#laydate_YY > label").click()
# arg2 = driver.find_element_by_id("laydate_ys").get_attribute("value")
# print(arg2)



