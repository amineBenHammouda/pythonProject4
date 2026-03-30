from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Base_URL= "https://practicetestautomation.com/practice-test-login/"

@given('i open the login page')
def step_open_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get(Base_URL)
    context.driver.maximize_window()
    
@when('i login with users from Excel')
def step_login_excel(context):
    for user in context.users:
        context.driver.get(Base_URL)
        username = user["username"]
        password = user["password"]

        username_locator = (By.ID, "username")
        password_locator = (By.ID, "password")
        login_button_locator = (By.ID, "submit")
        
        time.sleep(2)
        
        context.driver.find_element(*username_locator).send_keys(username)
        context.driver.find_element(*password_locator).send_keys(password)
        context.driver.find_element(*login_button_locator).click()
        time.sleep(2)