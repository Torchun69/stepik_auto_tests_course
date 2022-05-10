import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

text_alien = ''

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print(text_alien)

class TestAlien:
    links_massive = [("https://stepik.org/lesson/236895/step/1"),
                     ("https://stepik.org/lesson/236896/step/1"),
                     ("https://stepik.org/lesson/236897/step/1"),
                     ("https://stepik.org/lesson/236898/step/1"),
                     ("https://stepik.org/lesson/236899/step/1"),
                     ("https://stepik.org/lesson/236903/step/1"),
                     ("https://stepik.org/lesson/236904/step/1"),
                     ("https://stepik.org/lesson/236905/step/1")]

    @pytest.mark.parametrize('links', links_massive)
    def test_alien_stepik(self, browser, links):
        global text_alien
        link = f"{links}"
        browser.get(link)
        browser.implicitly_wait(10)
        answer = math.log(int(time.time() + 0.8))
        browser.find_element(By.CSS_SELECTOR, ".textarea").send_keys(str(answer))
        browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
        message_alien = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
        try:
            assert message_alien == "Correct!"
        except AssertionError:
            text_alien += message_alien
