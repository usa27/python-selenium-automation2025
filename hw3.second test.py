from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.target.com/')

driver.find_element(By.ID, 'search').send_keys('magic spoon')
driver.find_element(By.XPATH, "//button[@aria-label='search']").click()

sleep(2)

expected_text = 'magic spoon'
actual_text = driver.find_element(By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]").text
print(actual_text)

assert expected_text in actual_text, f'Expected text - {expected_text}, not in actual text - {actual_text}'
print('Test case PASSED')