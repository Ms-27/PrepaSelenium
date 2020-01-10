import pytest
from selenium import webdriver

def test_linktextloc():
    driver = webdriver.Chrome()
    driver.get('http://automationpractice.com/index.php')
    link_text = driver.find_element_by_link_text('Sign in').text
    print('Sign in Link text is: ' + link_text)