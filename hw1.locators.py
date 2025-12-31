from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
sign_in_url = 'https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'

driver.get(sign_in_url)

# CREATING LOCATORS + SEARCH STRATEGIES
# Amazon logo:
driver.find_element(By.XPATH, "//a[@class='a-link-nav-icon']")

#Email field:
driver.find_element(By.ID, 'ap_email').send_keys('hello')

# Continue button:
driver.find_element(By.XPATH, "//input[@type='submit']")

# Conditions of use link:
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

sleep(3)
# Need help link:
driver.find_element(By.XPATH, "//a[contains(@href, '/gp/help/customer/account-issues')]")

# Create a free business account link:
driver.find_element(By.XPATH,"//a[contains(@href, '/business/register')]")
driver.quit()