import time
from behave import *
from selenium import webdriver

@given('I launch Chrome browser')
def step_impl(context):
    #context.driver = webdriver.Chrome(executable_path="D:\Testing\Automated Testing\Frontend\Selenium\Python\selenium_python_challenge\chromedriver\chromedriver.exe")
    context.driver = webdriver.Chrome()

@when('I open saucedemo home page')
def step_impl(context):
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")


@when('Enter username "{user}" y password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_id("user-name").send_keys(user)
    context.driver.find_element_by_id("password").send_keys(pwd)

@when('Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("login-button").click()
    time.sleep(3)

@then('User must successfully login to the form page')
def step_impl(context):
    try:
        text = context.driver.find_element_by_xpath("//span[contains(text(),'Products')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text=="PRODUCTS":
        context.driver.close()
        assert True, "Test Passed"
