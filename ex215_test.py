import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_wait ():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://www.python.org')
    search_field = driver.find_element_by_id('id-search-field')
    search_field.send_keys('pytest')
    driver.find_element_by_id('submit').click()
    wait = WebDriverWait(driver, 10)
    title = driver.find_element_by_xpath("//h3[text()='Results']")
    wait.until(EC.visibility_of(title))