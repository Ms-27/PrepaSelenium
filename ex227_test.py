import pytest
from selenium import webdriver

def test_PO():
    driver = webdriver.Chrome()
    driver.get('http://automationpractice.com')
    