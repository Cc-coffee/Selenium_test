import unittest

import time
import sys
from automate_driver import AutomateDriver

"""
1. 导入 unittest
2. 继承 unittest.TestCase
3. 写用例 方法以 test 开头
4. 考虑使用 setUp() 和 tearDown()
"""


class Tests(unittest.TestCase):
    def setUp(self):
        """
        开始每个测试前的准备事项
        :return:
        """
        self.autoDriver = AutomateDriver()
        self.baseUrl = "https://demo.app.seedlinktech.com/drago/position/3870/"

    def tearDown(self):
        """
        结束每个测试后的清理工作
        :return:
        """
        self.autoDriver.quitBrowser()

    def test_seedlink_sign_in(self):
        """
        测试用例：测试登录
        :return:
        """
        self.autoDriver.navigate(self.baseUrl)

        print("注册测试开始")
        sys.stdout("zhucestart")
        self.autoDriver.click('l,开始')
        # 用name定位用户文本输入框
        #self.account_field = self.driver.find_element_by_id('sign-up-user-name')
        # # 用name定位密码文本输入框
        # self.captcha_field = self.driver.find_element_by_id('id_captcha_1')
        # self.account_field.clear()
        # self.captcha_field.clear()
        # self.driver.implicitly_wait(30)
        #
        # 输入用户名
        username = 'hongccoffee@163.com'
        # self.account_field.send_keys(username)
        self.autoDriver.type('id,sign-up-user-name', username)
        # # 输入密码
        # self.captcha_field.send_keys(input("输入正确的验证码："))
     #   input("输入正确的验证码：")
      #  self.autoDriver.type('id,id_captcha_1', "123")
        # # 使用js去点击勾选我已阅读并同意相关
        # js = "$('#privacy').click();"
        # self.driver.execute_script(js)
        # self.driver.implicitly_wait(30)
        #
        # time.sleep(1)
        # # 点击下一步
        # self.driver.find_element_by_id('login-next').click()
        #
        # # 手机或邮箱格式不对
        # error_info = self.driver.find_element_by_id('sign-up-invalid-user-name').text
        # print(error_info)
        # while error_info == "请输入手机或邮箱":
        #     self.account_field.clear()
        #     username = input("输入正确的手机或邮箱：")
        #     self.account_field.send_keys(username)
        #     time.sleep(1)
        #     self.driver.find_element_by_id('login-next').click()
        #     error_info = self.driver.find_element_by_id('sign-up-invalid-user-name').text
        # # 验证码不对
        # error_info = self.driver.find_element_by_id('sign-up-invalid-captcha').text
        # while error_info == "请正确输入图中文字或点击图片换一张":
        #     # ---------------ocr 识别验证码-----------------
        #     # print("验证码不对")
        #     # # 点击验证码图片
        #     # self.driver.find_element_by_css_selector("img.captcha").click()
        #     # self.driver.get_screenshot_as_file('D:\\image1.jpg')  # 比较好理解
        #     # code = get_code()
        #     # print(code)
        #     # ---------------------------------------------
        #     # ocr 识别率莫名极低 这里用手动输入
        #     self.captcha_field.clear()
        #     self.captcha_field.send_keys(input("输入正确的验证码："))
        #     time.sleep(1)
        #     self.driver.find_element_by_id('login-next').click()
        #     error_info = 0
        #     time.sleep(1)
        #     error_info = self.driver.find_element_by_id('sign-up-invalid-captcha').text
        # # 验证填写注册表单的url,没有直接注册的链接,首次登录就是填写个人信息，不管成功与否，二次登录只有忘记密码，这里为了方便就只写了忘记密码相关代码
        # currUrl = self.driver.current_url
        # if currUrl == "https://demo.app.seedlinktech.com/drago/answer/basic/?pid=3870":
        #     print("进入注册表单页面")
        # elif currUrl == "https://demo.app.seedlinktech.com/drago/candidate/login/?next=/drago" \
        #                 "/answer" \
        #                 "/basic/&pid=3870&login=true":
        #     print("进入忘记密码页面")
        #     self.driver.find_element_by_partial_link_text("忘记密码").click()
        #     # 填写帐号
        #     self_username_field = self.driver.find_element_by_id('userName')
        #     self_username_field.send_keys(username)
        #     # 点击获取验证码
        #     self.driver.find_element_by_id('codeBtn').click()
        #     # 验证码图片
        #     self_captcha_field = self.driver.find_element_by_id('id_captcha_1')
        #     self_captcha_field.clear()
        #     self_captcha_field.send_keys(input("输入正确的验证码："))
        #     # 填写新密码
        #     newpassword = 'Qq123456'
        #     self_newpassword_field = self.driver.find_element_by_id('new-password')
        #     self_newpassword_field.send_keys(newpassword)
        #     self_againpassword_field = self.driver.find_element_by_id('again-password')
        #     self_againpassword_field.send_keys(newpassword)
        #     # 填写短信验证码
        #     self_code02_field = self.driver.find_element_by_id('code02')
        #     self_code02_field.send_keys(input("短信验证码："))
        #
        #     # 点击重置密码
        #     # time.sleep(1)
        #     self.driver.find_element_by_id('reset').click()
        #     self.driver.implicitly_wait(10)
        #     # 检测输入数据是否合法
        #     error_info = self.driver.find_elements_by_xpath("//div[@role='info']")
        #     flag = 1
        #     while flag == 1:
        #         flag = 0
        #         for i in error_info:
        #             if i.text == "请正确输入图中文字或点击图片换一张":
        #                 self_captcha_field.clear()
        #                 self_captcha_field.send_keys(input("输入验证码图片文字~~："))
        #                 flag = 1
        #             if i.text == "请检查验证码":
        #                 self_code02_field.clear()
        #                 self_code02_field.send_keys(input("短信验证码："))
        #                 flag = 1
        #             if i.text == "您的密码长度须在8到20位之间，并至少包含以下4种类型中的3种：英文大写、英文小写、数字及符号。":
        #                 newpassword = input("重新输入新密码：")
        #                 flag = 1
        #                 self_newpassword_field.clear()
        #                 self_newpassword_field.send_keys(newpassword)
        #                 self_againpassword_field.clear()
        #                 self_againpassword_field.send_keys(newpassword)
        #         time.sleep(1)
        #         self.driver.find_element_by_id('reset').click()
        #         self.driver.implicitly_wait(30)
        #         # 查看是否有修改成功字样 TODO:第一次正确输入图片验证码时会弹出验证码错，手工输入没有，未能解决
        #         yes = self.driver.find_element_by_class_name('success').is_enabled()
        #         print(yes)
        #         if yes:
        #             break
        #
        #     # 注册成功有3秒延迟跳转，略过
        #     print("跳转中")
        #     time.sleep(1)
        #     currUrl = self.driver.current_url
        #     print(currUrl)
        #     if currUrl == "https://demo.app.seedlinktech.com/drago/candidate/reset/password/?from=jobseeker&pid=3870":
        #         print("注册成功1")
        #     elif currUrl == "https://demo.app.seedlinktech.com/drago/candidate/login/?signup=true":
        #         print("注册成功2")
        # else:
        #     print("urlerror")
        #
        # time.sleep(1)
        print("注册测试结束")

        time.sleep(5)

    def test_seedlink_login(self):
        """
        测试用例：测试登录
        :return:
        """
        #self.autoDriver.navigate("https://www.baidu.com")
        #time.sleep(5)
