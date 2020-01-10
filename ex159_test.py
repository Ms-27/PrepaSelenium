import pytest
from selenium import webdriver

def test_xpathloc():
    driver = webdriver.Chrome()
    driver.get('http://automationpractice.com/index.php')
    element = driver.find_element_by_xpath("//input[@id='search_query_top']")
    if element.is_displayed():
        print("l\'élément est présent")
    else:
        print("l\'élément n\'est pas présent")