from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ProductCheckout:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

        # Set locators for login
        self.user_name_locator = (By.CSS_SELECTOR, "#user-name")
        self.password_locator = (By.CSS_SELECTOR, "#password")
        self.button_login_locator = (By.CSS_SELECTOR, "#login-button")

        # Locators for cart_and_goods
        self.sauce_labs_bolt_t_shirt = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button")
        self.cart_locator = (By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a/span")

        # Checkout locators
        self.checkout_locator = (By.CSS_SELECTOR, "#checkout")

        # Checkout: Your Information locators
        self.first_name_locator = (By.CSS_SELECTOR, "#first-name")
        self.last_name_locator = (By.CSS_SELECTOR, "#last-name")
        self.postal_code_locator = (By.CSS_SELECTOR, "#postal-code")
        self.continue_button = (By.CSS_SELECTOR, "#continue")

        # Finish and back home buttons
        self.finish_button = (By.CSS_SELECTOR, "#finish")
        self.back_home_button = (By.CSS_SELECTOR, "#back-to-products")

    def open_page(self):
        self.driver.get(self.url)

    def login_in(self, user_name_data, password_data):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.user_name_locator)).send_keys(user_name_data)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_locator)).send_keys(password_data)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_login_locator)).click()
        
        except TimeoutException as e:
            print(f"Timeout error occurred while logging in: {e}")

    def add_goods(self):
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sauce_labs_bolt_t_shirt)).click()         
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cart_locator)).click()
            except TimeoutException as e:
                 print(f"Timeout error occurred while logging in: {e}")
            
                
        

    def checkout(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.checkout_locator)).click()
        except TimeoutException as e:
            print(f"Timeout error occurred during checkout: {e}")

    def checkout_information(self, first_name, last_name, postal_code):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.first_name_locator)).send_keys(first_name)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.last_name_locator)).send_keys(last_name)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.postal_code_locator)).send_keys(postal_code)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_button)).click()
        except TimeoutException as e:
            print(f"Timeout error occurred while entering checkout information: {e}")

    def finish_complete(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.finish_button)).click()
        except TimeoutException as e:
            print(f"Timeout error occurred while finishing and going back home: {e}")

    def back_to_main(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.back_home_button)).click()
        except TimeoutException as e:
            print(f"Timeout error occurred while finishing and going back home: {e}")
