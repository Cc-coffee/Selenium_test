# coding=utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


class WebDriverTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Chrome("D:\MyCode\Pycharm\Selenium_test\chromedriver\chromedriver.exe")
        cls.driver.get('about:blank')
        cls.driver.implicitly_wait(30)
        print(" -- set up finished -- ")
        print()

    def test_01_navigate(self):
        pass
        url_baidu = 'https://www.baidu.com/'
        url_zentao = 'http://pro.demo.zentao.net/user-login-Lw==.html'
        # 导航到百度
        self.driver.get(url_baidu)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # 导航到禅道
        self.driver.get(url_zentao)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # 后退
        self.driver.back()
        self.assertEqual(url_baidu, self.driver.current_url)
        self.driver.implicitly_wait(30)

        # 前进
        self.driver.forward()
        self.assertEqual(url_zentao, self.driver.current_url)
        self.driver.implicitly_wait(30)

        print("-- test 01 finished -- ")
        print()

    def test_02_element_interaction(self):
        self.driver.get('http://pro.demo.zentao.net')
        ## 找到用户名和密码的输入框
        self.account_field = self.driver.find_element_by_name('account')
        self.password_field = self.driver.find_element_by_name('password')
        ## 清除当前的输入
        self.account_field.clear()
        self.password_field.clear()
        self.driver.implicitly_wait(30)

        ## 输入用户名和密码，进行登录
        self.account_field.send_keys('demo')
        self.password_field.send_keys('123456')
        self.driver.find_element_by_id('submit').click()
        self.driver.implicitly_wait(30)

        companyname = self.driver.find_element_by_id('companyname')
        self.assertEqual('try项目管理系统', companyname.text)
        print(companyname.get_attribute('type'))
        print()
        self.driver.implicitly_wait(30)

        print('-- test 02 finished -- ')
        print()

    def test_03_element_interation2(self):
        ## 这里执行了一段JavaScript代码
        js = 'selectTheme("green")'
        self.driver.execute_script(js)
        self.driver.implicitly_wait(30)

        js = 'selectTheme("red")'
        self.driver.execute_script(js)
        self.driver.implicitly_wait(30)

        js = 'selectTheme("lightblue")'
        self.driver.execute_script(js)
        self.driver.implicitly_wait(30)

        js = 'selectTheme("blackberry")'
        self.driver.execute_script(js)
        self.driver.implicitly_wait(30)

        self.driver.find_element_by_link_text('产品').click()
        self.driver.implicitly_wait(30)

        self.driver.find_element_by_link_text('项目').click()
        self.driver.implicitly_wait(30)

        self.driver.find_element_by_link_text('退出').click()
        self.driver.implicitly_wait(30)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "submit")))

        self.driver.implicitly_wait(30)

        print('-- test 03 finished -- ')
        print()

    def test_04_cookies(self):

        self.driver.add_cookie(
            {'name': 'key-neeeeew', 'value': 'value-neeeewwwww'})

        # 遍历cookies 中的name 和value 信息打印，当然还有上面添加的信息
        for cookie in self.driver.get_cookies():
            print("%s -> %s" % (cookie['name'], cookie['value']))
            print()

        self.driver.delete_all_cookies()

        print("Del--")
        cookies = self.driver.get_cookies()
        print(cookies)
        print("cookie above")

        print('-- test 04 finished -- ')
        print()

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        #cls.driver.quit()
        pass
        print('-- tear down finished -- ')
        print()

if __name__ == '__main__':
    unittest.main(verbosity=2)