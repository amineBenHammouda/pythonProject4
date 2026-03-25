from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('the user is on the login page for outline')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()


@when('the user enters username "{username}" and password "{password}" for outline')
def step_enter_credentials(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(2)


@when('the user clicks the login button for outline')
def step_click_login(context):
    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(2)


@then('the result should be "{result}"')
def step_verify_result(context, result):
    if result == "success":
        # Vérifier qu'on est redirigé vers la page inventory
        assert context.driver.current_url != "https://www.saucedemo.com/", "Should be redirected from login page"
        context.driver.quit()
    elif result == "error_message":
        # Vérifier qu'il y a un message d'erreur
        error_message = context.driver.find_element(By.XPATH, "//div[@class='error-message-container error']").text
        assert "Epic sadface" in error_message or "Username and password do not match" in error_message, f"Expected error message but got: {error_message}"
        context.driver.quit()