import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SearchTests(unittest.TestCase):

    def setUp(self):
        # 创建一个新的浏览器对象
        self.driver = webdriver.Chrome("D:\MyCode\Pycharm\Selenium_test\chromedriver\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get('http://pro.demo.zentao.net')



    def test_search_by_category(self):

        # 用name定位用户文本输入框
        self.account_field = self.driver.find_element_by_name('account')
        # 用name定位密码文本输入框
        self.password_field = self.driver.find_element_by_name('password')
        self.account_field.clear()
        self.password_field.clear()
        self.driver.implicitly_wait(30)

        # 输入用户名demo
        self.account_field.send_keys('demo')
        # 输入密码123456
        self.password_field.send_keys('123456')
        self.driver.find_element_by_id('submit').click()
        self.driver.implicitly_wait(50)

        companyname = self.driver.find_element_by_id('companyname')
        self.assertEqual('demo项目管理系统', companyname.text)
        

    def tearDown(self):
        # 关闭浏览器对象
        #self.driver.quit()
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)