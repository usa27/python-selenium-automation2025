from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
RESULTS_COUNT = (By.CSS_SELECTOR, "[data-test='lp-resultsCount']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
CART_MESSAGE = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()

@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.wait.until(EC.visibility_of_element_located(CART_ICON))
    context.driver.find_element(*CART_ICON).click()


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    context.driver.wait.until(EC.visibility_of_element_located(RESULTS_COUNT))
    search_results_header = context.driver.find_element(*RESULTS_COUNT).text
    print(search_results_header)
    assert expected_product in search_results_header, f'Expected text {expected_product} not in {search_results_header}'

@then('Empty cart message is shown')
def verify_empty_cart_message(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(*CART_MESSAGE).text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} not in actual text {actual_text}'