# 测试框架是干什么用的
# 最主要的用途是组合和执行测试用例
# 可以写一个main()方法调用和执行所有的测试用例
# 1.导入unittest框架
import unittest
# java中类名和文件名的关系，public的类名和文件名一样
# python中的可以一样，但推荐：文件名首字母小写，类名首字母大写，剩下的一样
# 2.继承unittest中的父类
# python中的继承直接用自小括号表示
# 类的声明，在python中所有的{}都要用:代替
# TestCase 是测试用例的意思，UnittestDemo继承了unittest下面的TestCase这个类。我们就在UnitestDemo中编写测试用例
class UnittestDemo(unittest.TestCase):
    # 3.首先要重写父类中的方法setUp和tearDown
    # def 是方法的关键字
    # setUp 创建的意思
    #类似于手动测试中的预置条件
    def setUp(self):
        print("这个方法将会在测试用例执行前执行")

    def tearDown(self):
        print("这个方法将会在测试用例方法之后执行")

# 4.编写测试用例方法
    # 只有以test开头命名的方法才是测试用例方法
    # 测试用例方法可以直接被运行
    # 普通方法不能直接运行，只有被调用才能执行
    def test_login(self):
        print("登录测试用例")
        # zhu_ce()方法的调用
        self.zhu_ce()

    def zhu_ce(self):
        print("注册测试用例")

    def test_search(self):
        print("搜索测试用例")

# 两个下划线开头和结尾的方法是python内置的一些方法
# 如果你直接执行这个文件，那么就会执行下面的语句
# 否则，你执行其他文件，import这个文件的时候，下面的文件不会被执行
if __name__ == '__main__':
    # 执行当前文件中多有的unittest的测试用例
    # unittest.main()
    # 调用方法时，先对类进行实例化，然后再调用下面的方法
    UnittestDemo().zhu_ce()


