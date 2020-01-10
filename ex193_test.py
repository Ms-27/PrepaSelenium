import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

def test_alert():
    driver =webdriver.Chrome()
    driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert')
    frame = driver.find_element_by_id('iframeResult')
    driver.switch_to.frame(frame)
    button = driver.find_element_by_tag_name('button')
    button.click()
    alert = driver.switch_to.alert
    assert alert.text == 'Hello! I am an alert box!'
    alert.accept()
    