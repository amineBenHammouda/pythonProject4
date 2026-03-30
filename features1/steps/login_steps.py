from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('im on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()

@when('i enters username "standard_user" and password "secret_sauce"')
def step_impl(context):
    username_input = context.driver.find_element(By.ID, "user-name")
    password_input = context.driver.find_element(By.ID, "password")
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")


@when('i clicks the login button')
def step_impl(context):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()


@then('i should be redirected to the inventory page')
def step_impl(context):
    inventory_page = context.driver.find_element(By.CLASS_NAME, "inventory_list")
    assert inventory_page.is_displayed(), "Expected to be on the inventory page, but it was not displayed."


@given('im on the login page interface')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()


@when('i enters wrong username "invalid_user" and password "invalid_password"')
def step_impl(context):
    username_input = context.driver.find_element(By.ID, "user-name")
    password_input = context.driver.find_element(By.ID, "password")
    username_input.send_keys("invalid_user")
    password_input.send_keys("invalid_password")


@when('i click on the login button')
def step_impl(context):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(2)