from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_CARDS = (By.CSS_SELECTOR, '[data-test*="storycard"]')
BENEFIT_SMALL_CARDS = (By.CSS_SELECTOR, '.cell-item-content')
@given('Open Target circle page')
def open_circle(context):
    context.driver.get('https://www.target.com/circle')

@when('Target benefit cards are shown')
def benefit_cards(context):
    benefit_cards = context.driver.find_elements(*BENEFIT_CARDS)
    print(benefit_cards)
    benefit_small_cards = context.driver.find_elements(*BENEFIT_SMALL_CARDS)
    print(benefit_small_cards)

@then('Verify total benefit cards are shown')
def verify_benefit_cards_shown(context):
    benefit_cards = context.driver.find_elements(*BENEFIT_CARDS)
    benefit_small_cards = context.driver.find_elements(*BENEFIT_SMALL_CARDS)
    assert len(benefit_cards) > 1, f'Expected > 1 benefit cards, but got {len(benefit_cards)}'
    assert len(benefit_small_cards) > 1, f'Expected > 1 benefit cards, but got {len(benefit_small_cards)}'

