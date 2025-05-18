from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pytest import mark


def test_calendar():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    calendar = driver.find_element(By.ID,'datepicker')
    driver.execute_script('arguments[0].scrollIntoView()', calendar)
    time.sleep(2)
    calendar.click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class="ui-datepicker-next ui-corner-all"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class="ui-state-default" and @data-date="9"]').click()
    time.sleep(2)
    calendar.click()
    time.sleep(2)
    calendar.clear()
    time.sleep(2)
    calendar.send_keys('12/12/2025')
    time.sleep(5)
