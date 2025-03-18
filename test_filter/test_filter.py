from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from test_filter.web_part import TestFilter






@pytest.fixture(scope="session")
def driver_init():
    driver=webdriver.Chrome()
    m_f=TestFilter(driver)
    m_f.open_page()
    m_f.login_in("standard_user","secret_sauce")
    yield m_f



@pytest.mark.usefixtures("driver_init")
def test_filter_Name_A_to_Z(driver_init):
    driver_init.filter_Name_A_to_Z()
    product_elements=driver_init.driver.find_elements(By.CLASS_NAME,"inventory_item_name")
    product_names=[product.text for product in product_elements]
    sorted_product_names=sorted(product_names)
    assert product_names == sorted_product_names

@pytest.mark.usefixtures("driver_init")
def test_filter_Name_Z_to_A(driver_init):
    driver_init.filter_Name_Z_to_A()
    product_elements = driver_init.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_names = [product.text for product in product_elements]
    sorted_product_names = sorted(product_names, reverse=True)  
    assert product_names == sorted_product_names

@pytest.mark.usefixtures("driver_init")
def test_filter_price_low_to_high(driver_init):
    driver_init.filter_price_low_to_high()
    price_elements = driver_init.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(price.text.replace('$', '')) for price in price_elements]
    sorted_prices = sorted(prices)
    assert prices == sorted_prices

@pytest.mark.usefixtures("driver_init")
def test_filter_price_high_to_low(driver_init):
    driver_init.filter_price_high_to_low()
    price_elements = driver_init.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(price.text.replace('$', '')) for price in price_elements]
    sorted_prices = sorted(prices, reverse=True)
    assert prices == sorted_prices