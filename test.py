from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5000/signup")

time.sleep(2)

username_input = driver.find_element(By.NAME, "username")
username_input.send_keys("Tiger")

username_input = driver.find_element(By.NAME, "password")
username_input.send_keys("000")

submit_button = driver.find_element(By.CLASS_NAME, "loginBut")
submit_button.click()

time.sleep(4)
print("PAGE TITLE: ", driver.title)

driver.quit()