from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

def calc(x):
    return log(abs(12*sin(int(x))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
click1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()
time.sleep(1)
new_window = browser.window_handles[1]
sckip = browser.switch_to.window(new_window)
# alert = browser.switch_to.alert
# alert.accept()
# time.sleep(1)
x = int(browser.find_element(By.XPATH, '//*[@id="input_value"]').text)
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]').send_keys(str(y))
click2 = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()

time.sleep(5)

browser.quit()