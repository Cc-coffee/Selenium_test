import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SearchTests(unittest.TestCase):

    def setUp(self):
        # 创建一个新的浏览器对象
        self.driver = webdriver.Chrome("D:\MyCode\Pycharm\Selenium_test\chromedriver\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # 导航到京东主页
        self.driver.get("https://www.jd.com/")

    def test_search_by_category(self):
        # 获取到搜索框
        self.search_field = self.driver.find_element_by_id("key")
        self.search_field.clear()
        # 输入iphone 6s plus并按下回车进行搜索
        self.search_field.send_keys("iphone 6s plus"  + Keys.RETURN)
        # 获取所有的查询结果
        products = self.driver.find_elements_by_css_selector("li[class='gl-item']")
        # 断言：检查查询出来的个数是否为24个
        self.assertEqual(30, len(products))

    def tearDown(self):
        # 关闭浏览器对象
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)