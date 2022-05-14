from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_bascet_button(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    y = len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-two-basket"))
    assert y>0, '==КНОПКА НЕ НАЙДЕНА=='
