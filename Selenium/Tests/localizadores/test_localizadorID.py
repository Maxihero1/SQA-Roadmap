from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pytest import mark

def test_element_by_id():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")

    web_element = driver.find_element(By.ID, 'name')
    web_element.send_keys('Juan')

    actual_value = web_element.get_attribute('value')
    print(actual_value)

    time.sleep(5)
