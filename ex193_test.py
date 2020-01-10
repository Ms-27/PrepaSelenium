import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

def test_alert():
    driver =webdriver.Chrome()
    driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert')
    modal = driver.find_element_by_id('iframeResult')
    driver.switch_to.frame(modal)
    button = modal.find_element_by_tag_name('button')
    button.click()
    assert Alert.text == 'Hello! I am an alert box!'
    Alert.accept()
    