from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Start Chrome browser:
driver = webdriver.Chrome()
driver.get('https://stackoverflow.com/users/signup')

# Find the most optimal locators for StackOverflow Create Account page elements:

driver.find_element(By.XPATH, "//h1[text()='Create your account']")
driver.find_element(By.CSS_SELECTOR, "a[name='tos']")
driver.find_element(By.CSS_SELECTOR, "a[name='privacy']")
driver.find_element(By.CSS_SELECTOR, "#email")
driver.find_element(By.CSS_SELECTOR, "input#password")
driver.find_element(By.CSS_SELECTOR, ".c-pointer.js-show-password")
driver.find_element(By.CSS_SELECTOR, "#submit-button")
driver.find_element(By.CSS_SELECTOR, "button[data-provider='google']")
driver.find_element(By.CSS_SELECTOR, "button[data-provider='github']")
driver.find_element(By.CSS_SELECTOR, "[href*='/stackoverflow.com/teams']")