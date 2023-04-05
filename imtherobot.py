import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    answer = calc(x)

    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(answer)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
