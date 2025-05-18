from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from pytest import mark


def test_draganddrop():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    picture = driver.find_element(By.ID, 'draggable')

    target = driver.find_element(By.ID, 'droppable')

    driver.execute_script('arguments[0].scrollIntoView()', picture)
    action = ActionChains(driver)

    time.sleep(5)
    action.drag_and_drop(picture, target).perform()
    time.sleep(5)
