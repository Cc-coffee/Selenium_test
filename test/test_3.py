## 引入unittest模组
import unittest

## 定义测试类，名字为DemoTests
## 该类必须继承unittest.TestCase基类
class DemoTests(unittest.TestCase):

    ## 使用'@'修饰符，注明该方法是类的方法
    ## setUpClass方法是在执行测试之前需要先调用的方法
    ## 是开始测试前的初始化工作
    @classmethod
    def setUpClass(cls):
        pass

    ## 测试一（务必以test开头）
    def test_01(self):
        pass

    ## 测试二（务必以test开头）
    def test_02(self):
        pass

    ## 测试三（务必以test开头）
    def test_03(self):
        pass

    ## tearDownClass方法是执行完所有测试后调用的方法
    ## 是测试结束后的清除工作
    @classmethod
    def tearDownClass(cls):
        pass

# 执行测试主函数
if __name__ == '__main__':
    ## 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)