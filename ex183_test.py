import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

def test_dropdown():
    driver = webdriver.Chrome()
    driver.get('http://automationpractice.com/index.php?controller=prices-drop')
    dropdown = driver.find_element_by_id('selectProductSort')
    dropdown.click()
    option = driver.find_element_by_xpath("//select[@id='selectProductSort']/option[@value='quantity:desc']")
    option.click()