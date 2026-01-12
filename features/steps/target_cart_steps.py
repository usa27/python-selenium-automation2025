from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_CART_OPTIONS_BUTTON = (By.XPATH, "//button[contains(@id, 'addToCartButton')]")
PICK_UP_BUTTON = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
CARD_ITEM_TITLE = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')
WINDOW_CLOSE = (By.XPATH, "//button[@aria-label='close']")


@when('Click on add to cart icon')
def click_add_to_cart(context):
    sleep(15)
    context.driver.find_element(*ADD_CART_OPTIONS_BUTTON).click()

@when('Click Pick up button')
def click_pick_up_button(context):
    context.driver.find_element(*PICK_UP_BUTTON).click()

@when('Close added to cart window')
def close_added_window(context):
    context.driver.find_element(*WINDOW_CLOSE).click()

@then('Verify {expected_product} is added to cart')
def verify_add_to_cart(context, expected_product):
    sleep(5)
    cart_product_name = context.driver.find_element(*CARD_ITEM_TITLE).text
    print(cart_product_name)
    assert expected_product in cart_product_name.lower(), f'{expected_product} not in {cart_product_name}'

