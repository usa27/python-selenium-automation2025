from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_main(context):
    context.app.main_page.open_main_page()

@when('Search for {product}')
def search_product(context, product):
    context.app.header.search(product)

@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart()

@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)

@then('{empty_cart_msg} message is shown')
def verify_empty_cart_message(context, empty_cart_msg):
    context.app.cart_page.verify_cart_message(empty_cart_msg)