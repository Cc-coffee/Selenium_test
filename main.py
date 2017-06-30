import os
import unittest

import time

import pytesseract
from selenium import webdriver
import pytesser3
from PIL import Image, ImageEnhance
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class SearchTests(unittest.TestCase):
    def setUp(self):
        # 创建一个新的浏览器对象
        self.driver = webdriver.Chrome(
            "D:\MyCode\Pycharm\Selenium_test\chromedriver\chromedriver.exe")
        self.driver.implicitly_wait(30)
        # 最大化窗口
        # self.driver.maximize_window()

        self.driver.get('https://demo.app.seedlinktech.com/drago/position/3870/')

    def test_Sign_in(self):
        self.driver.find_element_by_link_text("开始").click()
        # 用name定位用户文本输入框
        self.account_field = self.driver.find_element_by_id('sign-up-user-name')
        # 用name定位密码文本输入框
        self.captcha_field = self.driver.find_element_by_id('id_captcha_1')
        self.account_field.clear()
        self.captcha_field.clear()
        self.driver.implicitly_wait(30)

        # 输入用户名demo
        self.account_field.send_keys('809683605@qq.com')
        # 输入密码123456
        self.captcha_field.send_keys('Qq123456')
        # 使用js去点击勾选我已阅读并同意相关
        js = "$('#privacy').click();"
        self.driver.execute_script(js)
        self.driver.implicitly_wait(30)

        yes = self.driver.find_element_by_id('login-next').is_enabled()
        print(yes)
        time.sleep(1)
        a = self.driver.find_element_by_id('login-next').click()

        # 手机或邮箱格式不对
        error_info = self.driver.find_element_by_id('sign-up-invalid-user-name').text
        print(error_info)
        while error_info == "请输入手机或邮箱":
            self.account_field.clear()
            self.account_field.send_keys(input("输入正确的手机或邮箱："))
            time.sleep(1)
            self.driver.find_element_by_id('login-next').click()
            error_info = self.driver.find_element_by_id('sign-up-invalid-user-name').text
        # 验证码不对
        error_info = self.driver.find_element_by_id('sign-up-invalid-captcha').text
        if error_info == "请正确输入图中文字或点击图片换一张":
            print("验证码不对")

            # -------------------对验证码进行区域截图，好吧，这方法有点low------------------

            self.driver.get_screenshot_as_file('D:\\image1.jpg')  # 比较好理解
            im = Image.open('D:\\image1.jpg')
            x = 235
            y = 660
            box = (x, y, x + 160, y + 60)  # 设置要裁剪的区域
            region = im.crop(box)  # 此时，region是一个新的图像对象。
            region.save("D:/image_code.jpg")
            # --------------------图片增强+自动识别简单验证码-----------------------------

            time.sleep(1)
            im = Image.open("D:\\image_code.jpg")
            imgry = im.convert('L')  # 图像加强，二值化
            sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
            sharp_img = sharpness.enhance(2.0)
            sharp_img.save("D:\\image_code.jpg")
            # time.sleep(3)  # 防止由于网速，可能图片还没保存好，就开始识别
            time.sleep(1)
            img = Image.open("D:\\image_code.jpg")
            code = pytesseract.image_to_string(img)
            print("------------")
            while True:
                captcha = self.driver.find_element_by_css_selector("img.captcha").click()
                self.driver.get_screenshot_as_file('D:\\image1.jpg')  # 比较好理解
                im = Image.open('D:\\image1.jpg')
                x = 235
                y = 660
                box = (x, y, x + 160, y + 60)  # 设置要裁剪的区域
                region = im.crop(box)  # 此时，region是一个新的图像对象。
                region.save("D:/image_code.jpg")
                # --------------------图片增强+自动识别简单验证码-----------------------------

                time.sleep(1)
                im = Image.open("D:\\image_code.jpg")
                imgry = im.convert('L')  # 图像加强，二值化
                sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
                sharp_img = sharpness.enhance(2.0)
                sharp_img.save("D:\\image_code.jpg")
                # time.sleep(3)  # 防止由于网速，可能图片还没保存好，就开始识别
                time.sleep(1)
                img = Image.open("D:\\image_code.jpg")
                code = pytesseract.image_to_string(img)
                print(code)

            # code即为识别出的图片数字str类型
            print(code)
            print("------------")
            print(code)

            # 打印code观察是否识别正确

        self.driver.implicitly_wait(300)


    def tearDown(self):
        # 关闭浏览器对象
        # self.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
