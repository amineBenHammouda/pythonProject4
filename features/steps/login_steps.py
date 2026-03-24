from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('the user is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com/')


@when('the user enters valid credentials')
def step_impl(context):
    username_input = context.driver.find_element(By.ID, 'user-name')
    password_input = context.driver.find_element(By.ID, 'password')
    username_input.send_keys('standard_user')
    password_input.send_keys('secret_sauce')


@when('clicks the login button')
def step_impl(context):
    login_button = context.driver.find_element(By.ID, 'login-button')
    login_button.click()


@then('the user should be redirected to the dashboard')
def step_impl(context):
    products_title = context.driver.find_element(By.CLASS_NAME, 'title')
    assert products_title.text == 'Products'
    time.sleep(5)
    context.driver.quit()

