from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_CART_OPTIONS_BUTTON = (By.XPATH, "//button[contains(@id, 'addToCartButton')]")
PICK_UP_BUTTON = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
CARD_ITEM_TITLE = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')
SIDE_NAV_CLOSE_BTN = (By.XPATH, "//button[@aria-label='close']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="content-wrapper"] h4')

@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')

@when('Click on add to cart icon')
def click_add_to_cart(context):
    sleep(15)
    context.driver.find_element(*ADD_CART_OPTIONS_BUTTON).click()
    context.driver.wait.until(
        EC.element_to_be_clickable(SIDE_NAV_CLOSE_BTN),
        message='Side navigation menu close button not clickable'
    )

@when('Store product name')
def store_product_name(context):
    context.product_before_adding = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text

@when('Click Pick up button')
def click_pick_up_button(context):
    context.driver.find_element(*PICK_UP_BUTTON).click()

@when('Close added to cart window')
def close_added_window(context):
    context.driver.find_element(*SIDE_NAV_CLOSE_BTN).click()

@then('Verify product in cart is correct')
def verify_add_to_cart(context):
    context.driver.wait.until(EC.presence_of_element_located((CARD_ITEM_TITLE)))
    product_in_cart = context.driver.find_element(*CARD_ITEM_TITLE).text
    expected = context.product_before_adding
    assert product_in_cart[:20] == expected[:20],\
        f'{product_in_cart[:20]} not in {expected[:20]}'

