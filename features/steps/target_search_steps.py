from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()

@when('Click on cart icon')
def click_cart_icon(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='lp-resultsCount']").text
    print(search_results_header)
    sleep(3)
    assert expected_product in search_results_header, f'Expected text {expected_product} not in {search_results_header}'

@then('Empty cart message is shown')
def verify_empty_cart_message(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]').text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} not in actual text {actual_text}'