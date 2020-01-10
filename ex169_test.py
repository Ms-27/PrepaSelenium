import pytest
from selenium import webdriver

def test_href():
    driver = webdriver.Chrome()
    driver.get('http://automationpractice.com/index.php')
    element = driver.find_element_by_class_name('login')
    value = element.get_attribute('href')
    print('href value of Sign in is: ' + value)
