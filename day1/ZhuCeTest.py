#1.打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()

#2.打开海盗商城的主页
#网址必须包含协议信息
driver.get("http://localhost/")

#3.点击注册链接
#第四种元素定位方法：链接的文本信息
driver.find_element_by_link_text("注册").click()
#往搜索框中输入tzh1118
#driver.find_element_by_name("keyword").send_keys("tzh1118")
#窗口切换：将selenium切换到新窗口工作
#handle 把手手柄
cwh = driver.current_window_handle  #属性，浏览器当前窗口的句柄（名字）
#print(cwh)
#selenium只提供了selenium工作的窗口的名字，并没有提供第二个窗口的名字，我们得自己求
whs = driver.window_handles   #浏览器中所有的窗口句柄
#for关键字(类型名 变量名:数组或其他集合){};(java)
#Python--for关键字_集合/数组中的某个元素 in关键字 数组/集合 冒号
#item表示whs中的一个元素，每次循环取一个值，循环结束，whs中的每个元素都会被遍历一次
#python语法：遇到冒号，下一行要空四个空格
#python的格式非常严格
#和for循环缩进程度一样，表示循环外面的代码
#for循环里的代码必须多缩进4个空格
for item in whs:
    if item == cwh:
        #.close()方法是关闭当前标签
        driver.close()
    else:
        #把selenium切换到第二个窗口
        driver.switch_to.window(item) #这种情况，item就是我们要找的窗口了，切换窗口方法swich_to.window()

#4.输入注册用户信息
driver.find_element_by_name("username").send_keys("tzh1118")
driver.find_element_by_name("password").send_keys("123654")
driver.find_element_by_name("userpassword2").send_keys("123654")
driver.find_element_by_name("mobile_phone").send_keys("13645614725")


#5.点击提交按钮