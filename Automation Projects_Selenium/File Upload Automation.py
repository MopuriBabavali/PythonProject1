from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")

driver.find_element(By.ID, "file-upload").send_keys(r"C:\Users\welcome\Desktop\testfile.txt")
driver.find_element(By.ID, "file-submit").click()

time.sleep(5)
driver.quit()
