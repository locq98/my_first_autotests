from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
from math import log, sin

def calc(x):
    return log(abs(12*sin(int(x))))

try:

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.XPATH, '//*[@id="input_value"]').text)
    y = calc(x)
    print(x)

    input3 = browser.find_element(By.XPATH, '//*[@id="answer"]').send_keys(str(y))
    browser.execute_script("window.scrollBy(0, 100);")

    input2 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]').click()
    input3 = browser.find_element(By.XPATH, '//*[@id="robotsRule"]').click()

    input1 = browser.find_element(By.XPATH, '/html/body/div/form/button').click()
    time.sleep(4)

finally:
    time.sleep(10)
    browser.quit()

