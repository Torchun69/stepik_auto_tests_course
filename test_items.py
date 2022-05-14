import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.fixture(scope="function")
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
