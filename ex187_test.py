import pytest
from selenium import webdriver

def test_modal():
    driver = webdriver.Chrome()
    driver.get('http://automationpractice.com')
    element = driver.find_element_by_xpath("//a[@title='Faded Short Sleeve T-shirts']")
    element.click()
    bouton = driver.find_element_by_xpath("//p[@id='add_to_cart']/button/span")
    bouton.click()
    modal = driver.find_element_by_id("layer_cart")
    bouton2 = modal.find_element_by_xpath("//a[@href=\"http://automationpractice.com/index.php?controller=order\"]")
    bouton2.click()
    assert driver.title == 'Order - My Store'