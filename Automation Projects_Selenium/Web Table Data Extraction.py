from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")

table = driver.find_element(By.ID, "customers")
rows = table.find_elements(By.TAG_NAME, "tr")

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    for col in cols:
        print(col.text, end=" | ")
    print()

driver.quit()
