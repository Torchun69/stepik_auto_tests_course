import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

languages = [
    ("ru", "русский"),
    ("de", "немецкий"),
    pytest.param("ua", "украинский",  marks=pytest.mark.xfail(reason="no ua language")),
    ("en-gb", "английский")
]

@pytest.mark.parametrize("code, lang", languages)
class TestLogin:
    def test_guest_should_see_login_link(self, browser, code, lang):
        link = "http://selenium1py.pythonanywhere.com/{}/".format(code)
        print("Проверяемый язык %s" % lang)
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
