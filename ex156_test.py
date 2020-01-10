import pytest
from selenium import webdriver

def test_linkloc():
    driver = webdriver.Chrome()
    driver.get('http://automationpractice.com/index.php')
    element = driver.find_element_by_link_text('Contact us')
    print(element.text)
    element2 = driver.find_element_by_partial_link_text('Conta')
    print(element2.text)