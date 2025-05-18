from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pytest import mark

def test_element_by_name():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")

    web_element = driver.find_element(By.NAME, 'start')
    web_element.click()

    time.sleep(5)
