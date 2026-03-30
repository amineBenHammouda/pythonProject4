from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('the user is on the wikipedia page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.wikipedia.org/")
    context.driver.maximize_window()


@when('the user enters "selenium" in the search bar')
def step_impl(context):
    search_bar = context.driver.find_element(By.ID, "searchInput")
    search_bar.clear()
    search_bar.send_keys("selenium")
    search_bar.send_keys(Keys.RETURN)


@then('the search results should display products related to "selenium"')
def step_impl(context):
    heading = WebDriverWait(context.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#firstHeading"))
    )
    assert "selenium" in heading.text.lower(), (
        f"Expected a selenium-related article heading, found '{heading.text}'"
    )