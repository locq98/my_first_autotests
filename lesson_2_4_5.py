from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")
button = browser.find_element(By.ID, ("button"))
button.click()

browser.quit()