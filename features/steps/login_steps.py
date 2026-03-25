from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage


@given('the user is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    
    
@when('the user enters username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    
@when('the user clicks the login button')
def step_click_login(context):
    context.login_page.click_login()
    
    
@then('the user should be redirected to the inventory page')
def step_verify_inventory_page(context):
    assert context.login_page.is_inventory_page_displayed(), "Inventory page is not displayed"
    context.driver.quit()        