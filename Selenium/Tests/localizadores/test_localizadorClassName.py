from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pytest import mark

@mark.locators
def test_element_by_name():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")

    web_element = driver.find_elements(By.CLASS_NAME, 'form-control')
    print('Cantidad de elementos class encontrados:', len(web_element))
    web_element[1].send_keys('test@hotmail.com')

    time.sleep(5)
