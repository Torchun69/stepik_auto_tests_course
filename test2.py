from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price_house = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100')    )
button = browser.find_element(By.ID, "book")
button.click()

x_element = browser.find_element(By.ID, 'input_value').text
x = int(x_element)
y = calc(x)
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

button = browser.find_element(By.ID, "solve")
button.click()

time.sleep(10)
browser.quit()
