## 引入WebDriver的包
from selenium import webdriver

## 创建浏览器对象
browser = webdriver.Chrome("D:\MyCode\Pycharm\Selenium_test\chromedriver\chromedriver.exe")

## 打开百度网站
browser.get('http://xyq.163.com//')