from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from biblioteca_test_case_1 import bibliotecaTest
from pytest import mark
from functions_test_case_1 import click_button, send_words, scroll_page, delete_words

@mark.login
def test_case_1():
    #Variables de funciones
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    #Apertura de driver
    driver.get('http://automationexercise.com')
    driver.maximize_window()

    # Pagina Principal
    click_button(driver, wait, By.XPATH, bibliotecaTest.MainPageSignUp_B)

    # Pagina de logeo
    send_words(driver, wait, By.NAME, bibliotecaTest.NewSignUpName_I, 'Pepe')
    send_words(driver, wait, By.XPATH, bibliotecaTest.NewSignUpEmail_I, 'pepe2@hotmail.com')
    click_button(driver, wait, By.XPATH, bibliotecaTest.NewSignUp_B)

    # Pagina de registro
    click_button(driver, wait, By.ID, bibliotecaTest.MaleGender_Checkbox)
    delete_words(driver, wait, By.ID, bibliotecaTest.RegisterUsername_I)
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterUsername_I, 'Dragoon')
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterPwd_I, 'Pepe123')
    scroll_page(driver, wait, By.ID, bibliotecaTest.RegisterBDay_C)
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterBDay_C, '17')
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterBMonth_C, 'November')
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterBYear_C, '2003')
    scroll_page(driver, wait, By.ID, bibliotecaTest.Newsletter_Checkbox)
    click_button(driver, wait, By.ID, bibliotecaTest.Newsletter_Checkbox)
    click_button(driver, wait, By.ID, bibliotecaTest.Offers_Checkbox)
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterFirstname_I, 'Pepe')
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterLastname_I, 'Perez')
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterUserCompany_I, 'Papalandia')
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterUserAdress1_I, 'Av. Mohammed')
    scroll_page(driver, wait, By.ID, bibliotecaTest.RegisterUserCountry_I)
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterUserCountry_I, 'Izrael')
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterUserState_I, 'Osama')
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterUserCity_I, 'Alibaba')
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterUserZip_I, '91000')
    send_words(driver, wait, By.ID, bibliotecaTest.RegisterUserMobile_I, '8091231234')
    click_button(driver, wait, By.XPATH, bibliotecaTest.RegisterCreateAccount_B)

    # Pagina de confirmacion de registro
    click_button(driver, wait, By.XPATH, bibliotecaTest.AccountCreated_B)

    # Pagina Principal logeada
    click_button(driver, wait, By.XPATH, bibliotecaTest.MainPageDeleteAcc_B)

    # Pagina de cuenta eliminada
    click_button(driver, wait, By.XPATH, bibliotecaTest.AccountDeleted_B)

    driver.quit()
