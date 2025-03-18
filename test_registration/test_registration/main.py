from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium .webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException




class TestLogin:
    def __init__(self,driver):
        self.driver=driver
        self.url="https://www.saucedemo.com/"

        #set locators
        self.user_name_locator=(By.CSS_SELECTOR,"#user-name")
        self.password_locator=(By.CSS_SELECTOR,"#password")
        self.button_login_locator=(By.CSS_SELECTOR,"#login-button")



    def open_page(self):
        self.driver.get(self.url)
    
    def login_in(self,user_name_data,password_data):
        try:
        
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.user_name_locator)).send_keys(user_name_data)
        
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.password_locator)).send_keys(password_data)
            
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.button_login_locator)).click()
        except NoSuchElementException as e:
            print(f"No such element error occurred: {e}")


        