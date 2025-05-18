from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from pytest import mark


def test_combobox():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')
    driver.maximize_window

    time.sleep(5)
    combobox = Select(driver.find_element(By.ID, 'country'))
    combobox.select_by_value('canada')
    time.sleep(5)
    combobox.select_by_visible_text('France')
    time.sleep(5)
