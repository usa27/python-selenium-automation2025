from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on Account')
def click_on_account(context):
    context.driver.find_element(By.CSS_SELECTOR, '#account-sign-in').click()

@when('Click on Sign In')
def click_signin(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]').click()

@then('Sign In form opened')
def signin_form(context):
    sleep(5)
    expected_text = 'Sign in or create account'
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text - {expected_text}, not in actual text - {actual_text}'