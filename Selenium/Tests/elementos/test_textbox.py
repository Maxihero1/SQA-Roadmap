from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pytest import mark


def test_textbox():
    driver = webdriver.Chrome()
    driver.get('https://www.lambdatest.com/selenium-playground/iframe-demo/')

    frame_element = driver.find_element(By.ID, 'iFrame1')
    driver.switch_to.frame(frame_element)

    actual_value = driver.find_element(By.CLASS_NAME, 'rsw-ce').get_attribute('value')
    print(actual_value)
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, 'rsw-ce').clear()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, 'rsw-ce').send_keys('Hola, soy yo.')
    time.sleep(5)
