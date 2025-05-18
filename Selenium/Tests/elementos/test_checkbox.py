from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pytest import mark


def test_checkbox():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    checkbox = driver.find_element(By.ID, 'sunday')

    driver.execute_script('arguments[0].scrollIntoView()', checkbox)
    time.sleep(4)
    checkbox.click()
    time.sleep(4)
    driver.execute_script('arguments[0].click()', checkbox)
    time.sleep(4)

    print('El elemento es:', checkbox.get_attribute('type'))
    print('El checkbox esta seleccionado:', checkbox.is_selected())
    time.sleep(4)
