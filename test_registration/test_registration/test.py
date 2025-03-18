from selenium import webdriver
import pytest
from test_registration.main import TestLogin

# Define the fixture for the driver initialization
@pytest.fixture(scope="function")
def driver_init():
    driver = webdriver.Chrome()
    main = TestLogin(driver)
    main.open_page() 
    yield main
    

# Parameterized test for login functionality
@pytest.mark.parametrize("user_name,password", [
    ("user_1", "password_1"),
    ("user_2", "password_2"),
    ("user_03", "password_03"),
    ("user_04", "password_04"),
    ("standard_user", "secret_sauce")
], ids=[
    "Test_User1_Login", 
    "Test_User2_Login", 
    "Test_User3_Login",
    "Test_User4_Login", 
    "Test_Standard_User_Login"
])
@pytest.mark.usefixtures("driver_init")  # Use the driver_init fixture
def test_login(driver_init, user_name, password):
    driver_init.login_in(user_name,password)
    current_url = driver_init.driver.current_url
    assert "inventory" in current_url