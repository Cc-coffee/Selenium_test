#coding=utf-8
from selenium import webdriver
#引入Keys 类包
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("D:\MyCode\Pycharm\Selenium_test\chromedriver\chromedriver.exe")
driver.get("http://www.baidu.com")
#输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)
#删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(3)
#输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
time.sleep(3)
#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')