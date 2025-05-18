from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_button(driver, wait, type, value):
    clickable = wait.until(EC.visibility_of_element_located((type, value)))
    clickable.click()

def send_words(driver, wait, type, value, text):
    words = wait.until(EC.presence_of_element_located((type, value)))
    words.send_keys(text)

def delete_words(driver, wait, type, value):
    words = wait.until(EC.presence_of_element_located((type, value)))
    words.clear()
    
def scroll_page(driver, wait, type, value):
    element = wait.until(EC.presence_of_element_located((type, value)))
    driver.execute_script('arguments[0].scrollIntoView()', element)
