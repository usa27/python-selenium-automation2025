from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page

class SearchResultsPage(Page):
    RESULTS_COUNT = (By.CSS_SELECTOR, "[data-test='lp-resultsCount']")

    def verify_search_results(self, expected_product):
        self.driver.wait.until(EC.visibility_of_element_located(self.RESULTS_COUNT))
        actual_text = self.driver.find_element(*self.RESULTS_COUNT).text
        assert expected_product in actual_text, f'Expected text {expected_product} not in {actual_text}'
