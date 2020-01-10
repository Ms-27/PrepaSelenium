from selenium import webdriver
import pytest

def test_doc():
    driver = webdriver.Chrome()
    driver.get('https://www.python.org')
    element = driver.find_element_by_xpath('//a[@href="/doc/"]')
    element.click()
    #assert 'Our Documentation' in driver.title
    assert driver.title == 'Our Documentation | Python.org', "Pas le bon titre de page"
    driver.quit()