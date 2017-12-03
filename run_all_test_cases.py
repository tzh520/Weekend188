import unittest


if __name__ == '__main__':
    # defaltTestLoader 默认测试用例加载器，用于寻找符合一定规则的测试用例
    # discover 发现（寻找）
    # "*Test.py" 任意字符开头，以Test.py结尾的文件，*是通配符，表示任意字符
    # suite 套，组
    suite = unittest.defaultTestLoader.discover("./day5", pattern='*Test.py')
    # 执行suite中的所有的测试用例
    # TextTestRuuner 文本的测试用例 运行器，返回结果是一段文本日志，所以叫文本
    # TextTestRunner 首字母大写，说明它是一个类，类不能直接调用方法
    # 必须实例化对象才能调用方法
    # python中实例化不需要new关键字，直接在类后面加一对小括号就可以了
    unittest.TextTestRunner().run(suite)
    # 运行结果中的".F"表示，运行两个测试用例及其运行结果，"." 表示测试用例通过，"F"表示测试用例失败
