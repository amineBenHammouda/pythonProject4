from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

Base_URL = "https://parabank.parasoft.com/parabank/register.htm"
fake=Faker()

@given('i open the register page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(Base_URL)
    context.driver.maximize_window()
    time.sleep(2)
    
    
@when('i enter a unique username')
def step_impl(context):
    context.username = fake.user_name()
    context.driver.find_element(By.NAME, "customer.username").send_keys(context.username)
    time.sleep(2)
    