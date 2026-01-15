from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):
    CART_MESSAGE = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

    def verify_cart_message(self, empty_cart_msg):
        actual_text = self.driver.find_element(*self.CART_MESSAGE).text
        assert empty_cart_msg in actual_text, f' Expected message {empty_cart_msg} not in actual text {actual_text}'