import pytest
from selenium import webdriver

def test_browsers():
    drv1 = webdriver.Chrome()
    drv2 = webdriver.Chrome()
    drv1.get('https://www.python.org')
    drv2.get('https://www.w3.org/')
    assert drv1.title == 'Welcome to Python.org'
    assert drv2.title == 'World Wide Web Consortium (W3C)'
    drv1.get_screenshot_as_file('C:\\Users\\formation\\Desktop\\screenshot1.png')
    drv2.get_screenshot_as_file('C:\\Users\\formation\\Desktop\\screenshot2.png')
    drv1.quit()
    drv2.quit()