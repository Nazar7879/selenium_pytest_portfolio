from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


class TestFilter:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

        # set locators for login
        self.user_name_locator = (By.CSS_SELECTOR, "#user-name")
        self.password_locator = (By.CSS_SELECTOR, "#password")
        self.button_login_locator = (By.CSS_SELECTOR, "#login-button")

        # set locators for filter
        self.filter_locator = (By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select")

    def open_page(self):
        self.driver.get(self.url)

    def login_in(self, user_name_data, password_data):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.user_name_locator)
            ).send_keys(user_name_data)

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.password_locator)
            ).send_keys(password_data)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.button_login_locator)
            ).click()
        except NoSuchElementException as e:
            print(f"No such element error occurred: {e}")
      

    def filter_Name_A_to_Z(self):
        filter_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.filter_locator)
        )
        filter_element.click()
        select = Select(filter_element)
        select.select_by_visible_text("Name (A to Z)")
       

    def filter_Name_Z_to_A(self):
        filter_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.filter_locator)
        )
        select = Select(filter_element)
        select.select_by_visible_text("Name (Z to A)")
        
    def filter_price_low_to_high(self):
        filter_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.filter_locator)
        )
        select = Select(filter_element)
        select.select_by_visible_text("Price (low to high)")
  

    def filter_price_high_to_low(self):
        filter_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.filter_locator)
        )
        select = Select(filter_element)
        select.select_by_visible_text("Price (high to low)") 
       

    



    


        