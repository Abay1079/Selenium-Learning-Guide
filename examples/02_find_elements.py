from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

# Find search box and type a query
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Selenium (software)")
search_box.submit()

print("Current URL:", driver.current_url)

driver.quit()

