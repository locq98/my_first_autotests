from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")
button = browser.find_element(By.XPATH, ("//*[@id='verify']"))
button.click()
browser.implicitly_wait(5)
message = browser.find_element(By.ID, "verify_message")

assert message.text == "Verification was successful!"

browser.quit()