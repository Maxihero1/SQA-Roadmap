from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pytest import mark

def test_elements_by_xpath():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    driver.find_element(By.XPATH, '//*[@id="HTML5"]/div[1]/button').click()
    print('Xpath')
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[2]/div[1]/button').click()
    print('Full Xpath')
    time.sleep(5)
    driver.find_element(By.XPATH, '//button[@name="start" and @class="start"]').click()
    print('Custom Xpath')
    time.sleep(5)
