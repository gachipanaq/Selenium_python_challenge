import time
from behave import *
from selenium import webdriver

@given('I launch browser')
def step_impl(context):
    #context.driver = webdriver.Chrome(executable_path="D:\Testing\Automated Testing\Frontend\Selenium\Python\Python_selenium_challenge\drivers\chromedriver.exe")
    context.driver = webdriver.Chrome()

@when('I open application')
def step_impl(context):
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")

@when('Enter username "{user}" and password "{pwd}"')
def login(context, user, pwd):
    context.driver.find_element_by_id("user-name").send_keys(user)
    context.driver.find_element_by_id("password").send_keys(pwd)

@when('Click on login')
def step_impl(context):
    context.driver.find_element_by_id("login-button").click()

@when('Navigate to buy page')
def step_impl(context):
    text = context.driver.find_element_by_xpath("//span[contains(text(),'Products')]").text
    assert text=="PRODUCTS"

@step('Add cart')
def step_impl(context):
    context.driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
    time.sleep(3)
    context.driver.find_element_by_class_name("shopping_cart_link").click()
    time.sleep(3)

@step('Add more cart')
def step_impl(context):
    context.driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
    context.driver.find_element_by_id("add-to-cart-sauce-labs-bike-light").click()
    context.driver.find_element_by_id("add-to-cart-sauce-labs-bolt-t-shirt").click()
    time.sleep(3)
    context.driver.find_element_by_class_name("shopping_cart_link").click()
    time.sleep(3)

@step('Checkout cart')
def step_impl(context):
    context.driver.find_element_by_id("checkout").click()
    time.sleep(2)

@step('Enter information')
def step_impl(context):
    context.driver.find_element_by_id("first-name").send_keys("Gherard")
    time.sleep(1)
    context.driver.find_element_by_id("last-name").send_keys("Chipana")
    time.sleep(1)
    context.driver.find_element_by_id("postal-code").send_keys("Lima 01")
    time.sleep(1)
    context.driver.find_element_by_id("continue").click()
    time.sleep(2)

@step('Checkout overview')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 400);")
    time.sleep(2)
    context.driver.find_element_by_id("finish").click()

@when('Checkout complete')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 0);")
    text = context.driver.find_element_by_xpath("//h2[contains(text(),'THANK YOU FOR YOUR ORDER')]").text
    assert text=="THANK YOU FOR YOUR ORDER"
    time.sleep(2)

@then('Logout')
def step_impl(context):
    context.driver.find_element_by_id("react-burger-menu-btn").click()
    time.sleep(3)

    context.driver.find_element_by_id("logout_sidebar_link").click()
    time.sleep(2)