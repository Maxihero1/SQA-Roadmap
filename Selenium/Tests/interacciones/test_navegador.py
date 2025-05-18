from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pytest import mark


def test_navegador():
    driver = webdriver.Chrome()

    driver.get('https://www.youtube.com/')
    print(driver.current_url)

    search = driver.find_element(By.NAME, 'search_query')
    search.send_keys('Hey', Keys.ENTER)
    time.sleep(2)

    driver.back()    
    time.sleep(2)

    driver.forward()
    time.sleep(2)

    driver.refresh()
    time.sleep(5)
