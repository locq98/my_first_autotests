from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin

def calc(x):
    return log(abs(12*sin(int(x))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '100')
)
message = browser.find_element(By.ID, "book").click()
x = int(browser.find_element(By.XPATH, '//*[@id="input_value"]').text)
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]').send_keys(str(y))
click2 = browser.find_element(By.XPATH, '//*[@id="solve"]').click()

browser.quit()