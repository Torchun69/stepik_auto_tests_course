from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

def link_t(link):

        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block .second')
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block .third')
        input3.send_keys("Ivanov@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR,"button.btn")
        button.click()

        time.sleep(5)
        return browser.find_element(By.TAG_NAME, "h1").text


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!", "Register is FAILED")
    def test_abs2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),"Congratulations! You have successfully registered!", "Register is FAILED")

if __name__ == "__main__": unittest.main()
