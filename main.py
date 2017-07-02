# -*- utf-8 -*-
import unittest
import time
import pytesseract
from selenium import webdriver
from PIL import Image, ImageEnhance
from automate_driver import AutomateDriver

username = 'hongccoffee@163.com'
newPassword = 'Qq123456'


# 解析验证码图片文字
def get_code():
    # -------------------对验证码进行区域截图------------------
    im = Image.open('D:\\image1.jpg')
    x = 235
    y = 660
    box = (x, y, x + 160, y + 60)  # 设置要裁剪的区域
    region = im.crop(box)  # 此时，region是一个新的图像对象。
    region.save("D:/image_code.jpg")
    # --------------------图片增强+自动识别简单验证码-----------------------------
    im = Image.open("D:\\image_code.jpg")
    imgry = im.convert('L')  # 图像加强，二值化
    sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
    sharp_img = sharpness.enhance(2.0)
    sharp_img.save("D:\\image_code.jpg")
    img = Image.open("D:\\image_code.jpg")
    code = pytesseract.image_to_string(img)
    return code


class SeedLinkTests(unittest.TestCase):
    def setUp(self):
        # 创建一个新的浏览器对象
        self.autoDriver = AutomateDriver()

    def tearDown(self):
        # 关闭浏览器对象
        self.autoDriver.quitBrowser()
        pass

    def test_01_Sign_in(self):
        # 打开网页
        self.autoDriver.navigate('https://demo.app.seedlinktech.com/drago/position/3870/')
        print()
        print("注册测试开始")
        self.autoDriver.click('link_text,开始')
        # 输入用户名
        self.autoDriver.type('id,sign-up-user-name', username)
        # 输入验证码
        self.autoDriver.type('id,id_captcha_1', input("输入正确的验证码："))
        # 使用js去点击勾选我已阅读并同意相关
        js = "$('#privacy').click();"
        self.autoDriver.executeJs(js)
        time.sleep(1)
        # 点击下一步
        self.autoDriver.click('id,login-next')
        # 手机或邮箱格式不对
        error_info = self.autoDriver.getText('id,sign-up-invalid-user-name')
        print(error_info)
        while error_info == "请输入手机或邮箱":
            self.autoDriver.type('id,sign-up-user-name', input("输入正确的手机或邮箱："))
            time.sleep(1)
            self.autoDriver.click('id,login-next')
            error_info = self.autoDriver.getText('id,sign-up-invalid-user-name')
        # 验证码不对
        error_info = self.autoDriver.getText('id,sign-up-invalid-captcha')
        while error_info == "请正确输入图中文字或点击图片换一张":
            # ---------------ocr 识别验证码-----------------
            # print("验证码不对")
            # # 点击验证码图片
            # self.driver.find_element_by_css_selector("img.captcha").click()
            # self.driver.get_screenshot_as_file('D:\\image1.jpg')  # 比较好理解
            # code = get_code()
            # print(code)
            # ---------------------------------------------
            # ocr 识别率莫名极低 这里用手动输入
            self.autoDriver.type('id,id_captcha_1', input("输入正确的验证码："))
            time.sleep(1)
            self.autoDriver.click('id,login-next')
            error_info = 0
            time.sleep(1)
            error_info = self.autoDriver.getText('id,sign-up-invalid-captcha')
        # 验证填写注册表单的url,没有直接注册的链接,首次登录就是填写个人信息，不管成功与否，二次登录只有忘记密码.
        # 这里为了方便就只写了忘记密码相关代码
        currUrl = self.autoDriver.getUrl()
        if currUrl == "https://demo.app.seedlinktech.com/drago/answer/basic/?pid=3870":
            print("进入注册表单页面")
        elif currUrl == "https://demo.app.seedlinktech.com/drago/candidate/login/?next=/drago" \
                        "/answer" \
                        "/basic/&pid=3870&login=true":
            print("进入忘记密码页面")
            self.autoDriver.click('link_text,忘记密码')
            # 填写帐号
            self.autoDriver.type('id,userName', username)
            # 点击获取验证码
            self.autoDriver.click('id,codeBtn')
            # 填写新密码
            self.autoDriver.type('id,new-password', newPassword)
            self.autoDriver.type('id,again-password', newPassword)
            # 填写短信验证码
            self.autoDriver.type('id,code02', input("短信验证码："))
            time.sleep(1)
            # 验证码图片
            self.autoDriver.type('id,id_captcha_1', input("输入验证码图片："))
            time.sleep(1)
            # 点击重置密码
            self.autoDriver.click('id,reset')
            # 检测输入数据是否合法,一执行重置密码就会更换验证码图片，手动输入时没有问题
            error_info = self.autoDriver.getElements('xpath,//div[@role="info"]')
            flag = 1
            while flag == 1:
                flag = 0
                for i in error_info:
                    if i.text == "请检查验证码":
                        self.autoDriver.type('id,code02', input("短信验证码："))
                        flag = 1
                    if i.text == "您的密码长度须在8到20位之间，并至少包含以下4种类型中的3种：英文大写、英文小写、数字及符号。":
                        flag = 1
                        pass
                    if i.text == "请正确输入图中文字或点击图片换一张":
                        flag = 1
                        self.autoDriver.type('id,id_captcha_1', input("输入验证码图片："))
                if flag == 1:
                    time.sleep(5)  # 略过上一次的错误信息
                    self.autoDriver.click('id,reset')
                    time.sleep(1)
                    error_info = self.autoDriver.getElements('xpath,//div[@role="info"]')
            time.sleep(2)
            yes = self.autoDriver.getDisplay('class_name,success')
            yes = self.autoDriver.getDisplay('class_name,success')
            time.sleep(1)
            if yes:
                print("注册成功")
                time.sleep(3)
            else:
                print("没成功")
        else:
            print("urlerror")
        time.sleep(1)
        print("注册测试结束")

    def test_02_Log_in(self):
        # 打开网页
        self.autoDriver.navigate(
            'https://demo.app.seedlinktech.com/drago/candidate/login/?signup=true')
        print()
        print("登录测试开始")
        # 主页面
        currUrl = self.autoDriver.getUrl()
        print(currUrl)
        if currUrl == "https://demo.app.seedlinktech.com/drago/candidate/login/?signup=true":
            # 填写用户名
            self.autoDriver.type('id,sign-up-user-name', username)
            # 填写验证码
            self.autoDriver.type('id,id_captcha_1', input("输入正确的验证码："))
            # 执行js
            js = "$('#privacy').click();"
            self.autoDriver.executeJs(js)
            time.sleep(1)
            # 点击下一步
            self.autoDriver.click('id,login-next')
            time.sleep(1)
            # 获取错误信息
            error_info = self.autoDriver.getText('id,sign-up-invalid-captcha')
            while error_info == "请正确输入图中文字或点击图片换一张":
                self.autoDriver.type('id,id_captcha_1', input("重新输入正确的验证码："))
                time.sleep(1)
                self.autoDriver.click('id,login-next')
                time.sleep(1)
                error_info = 0
                error_info = self.autoDriver.getText('id,sign-up-invalid-captcha')
        # 登录页面
        time.sleep(1)
        currUrl = self.autoDriver.getUrl()
        print(currUrl)
        if currUrl == "https://demo.app.seedlinktech.com/drago/candidate/login/?login=true":
            # 填写密码
            self.autoDriver.type('id,log-in-password', newPassword)
            time.sleep(1)
            # 提交
            self.autoDriver.click('xpath,//button[@type="submit"]')
            time.sleep(1)
        # 本想用url验证登录，但获取到的url和浏览器的url不一致，也不知道原因
        # currUrl = self.autoDriver.getUrl()
        # print(currUrl)
        # if currUrl == "https://demo.app.seedlinktech.com/drago/":
        #     print("登录成功")
        # else:
        #     print("登录失败")
        # 用页面存在的元素验证是否登录成功
        time.sleep(3)
        self.myinfo_field = self.autoDriver.getElement('xpath,//*[@data-item-type="menu"]')
        if self.myinfo_field.is_enabled():
            print("登录成功")
        else:
            print("登录失败")
        time.sleep(3)
        print("登录测试结束")


if __name__ == '__main__':
    unittest.main(verbosity=2)
