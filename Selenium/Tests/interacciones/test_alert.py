from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from pytest import mark

@mark.page
def test_alert():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    alert_B = driver.find_element(By.ID, 'alertBtn')

    driver.execute_script('arguments[0].scrollIntoView()', alert_B)
    
    alert_B.click()

    time.sleep(3)

    alert = Alert(driver)

    alert.accept()

    time.sleep(3)
