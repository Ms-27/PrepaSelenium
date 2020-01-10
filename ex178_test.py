import pytest
from selenium import webdriver

def test_openpage():
    driver = webdriver.Chrome()
    driver.get('http://automationpractice.com/index.php')
    element = driver.find_element_by_link_text('Sign in')
    element.click()
    assert driver.title == 'Login - My Store'