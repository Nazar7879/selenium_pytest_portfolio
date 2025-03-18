from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from cart_and_goods.main_checkout import ProductCheckout


@pytest.fixture(scope="session")
def init_driver():
    driver=webdriver.Chrome()
    checkout_page=ProductCheckout(driver)
    checkout_page.open_page()
    yield  checkout_page






pytest.mark.usefixtures("init_driver")

def test_login_in(init_driver):
    init_driver.login_in(user_name_data="standard_user",password_data="secret_sauce")
    current_url=init_driver.driver.current_url
    assert "inventory" in current_url



pytest.mark.usefixtures("init_driver")

def test_add_goods(init_driver):
     init_driver.add_goods()
     cart_item = init_driver.driver.find_element(By.CSS_SELECTOR, "#item_1_title_link > div")
     assert "Sauce Labs Bolt T-Shirt" in cart_item.text


@pytest.mark.parametrize(
    "first_name,last_name,postal_code",
    [("test", "test", "a5d5n6")]
)
@pytest.mark.usefixtures("init_driver")
def test_checkout_step_1(init_driver,first_name,last_name,postal_code):
    init_driver.checkout()
    current_url=init_driver.driver.current_url
    init_driver.checkout_information(first_name,last_name,postal_code)
    assert "checkout-step-one" in current_url

@pytest.mark.usefixtures("init_driver")
def test_checkout_step_2(init_driver):
     current_url=init_driver.driver.current_url
     assert "checkout-step-two" in current_url


@pytest.mark.usefixtures("init_driver")
def test_checkout_step_3(init_driver):
    init_driver.finish_complete()
    current_url=init_driver.driver.current_url
    assert "checkout-complete" in current_url


@pytest.mark.usefixtures("init_driver")
def test_back_to_main(init_driver):
    init_driver.back_to_main()
    current_url=init_driver.driver.current_url
    assert "inventory" in current_url

    






