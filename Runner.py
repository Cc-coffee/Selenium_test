# -*- utf-8 -*-
import unittest
from Tests_case import Tests
import HTMLTestRunner


class TestRunner():
    def runTest(self):
        """
        运行测试用例
        :return:
        """
        # 声明一个测试套件
        suite = unittest.TestSuite()

        # 添加测试用例到测试套件
        suite.addTest(Tests("test_seedlink_sign_in"))
        suite.addTest(Tests("test_seedlink_login"))

        # 创建一个新的测试结果文件
        buf = open("./result.html", "wb")

        # 声明测试运行的对象
        runner = HTMLTestRunner.HTMLTestRunner(stream=buf,
                                               title="Test Result",
                                               description="Test Case Run Result")

        # 运行测试，并且将结果生成为HTML
        runner.run(suite)


if __name__ == "__main__":
    # 实例化一个runner
    runner = TestRunner()
    # 执行测试
    runner.runTest()
