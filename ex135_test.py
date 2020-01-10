import pytest
from selenium import webdriver

def test_iframe ():
    driver = webdriver.Chrome()
    driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert')
    driver.maximize_window()
    driver.switch_to.frame('iframeResult')
    driver.switch_to.default_content()
    driver.quit()
    