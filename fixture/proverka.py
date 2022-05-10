from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import math

final = ''


@pytest.fixture(scope="session")
def browser():
    br = webdriver.Chrome()
    yield br
    br.quit()
    print(final)  # напечатать ответ про Сов в конце всей сессии


@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_find_hidden_text(browser, lesson):
    global final
    link = f'https://stepik.org/lesson/{lesson}/step/1'
    browser.implicitly_wait(10)
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, 'textarea').send_keys(str(answer))
    browser.find_element(By.CSS_SELECTOR, '.submit-submission ').click()
    check_text = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    try:
        assert 'Correct!' == check_text
    except AssertionError:
        final += check_text  # собираем ответ про Сов с каждой ошибкой
