import pytest
from selenium import webdriver
from time import sleep

def test_chckbox():
    driver = webdriver.Chrome()
    driver.get('http://automationpractice.com/index.php?id_category=8&controller=category#/categories-casual_dresses/compositions-cotton')
    checkbox = driver.find_element_by_id('layered_id_attribute_group_1')
    if checkbox.is_selected():
        print ('La taille S est cochée')
    else:
        print("La taille S n\'est pas cochée")
    sleep(3)
    if checkbox.is_selected():
        print ('La taille S est cochée')
    else:
        print("La taille S n\'est pas cochée")