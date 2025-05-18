from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark
import time

def test_loginoym():
    driver = webdriver.Chrome()
    driver.get('https://login.oymas.edu.do/v2/')

    driver.find_element(By.ID, 'user').send_keys('usuario')
    time.sleep(2)
    driver.find_element(By.ID, 'password').send_keys('contraseña')
    time.sleep(2)
    driver.find_element(By.ID, 'Login').click()
    time.sleep(10)
