from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    
    
@when('the user enters wrong username "invalid_user" and password "invalid_password"')
def step_enter_wrong_credentials(context):
    context.login_page.enter_username("invalid_user")
    context.login_page.enter_password("invalid_password")
    context.login_page.click_login()
    
@then('the user should see an error message')
def step_verify_error_message(context):
    error_message = context.driver.find_element(By.XPATH, "//div[@class='error-message-container error']").text
    assert "Epic sadface" in error_message or "Username and password do not match" in error_message, f"Expected error message but got: {error_message}"
    context.driver.quit()