from selenium import webdriver

# Open Chrome and visit Google
driver = webdriver.Chrome()
driver.get("https://www.google.com")

print("Page title is:", driver.title)

driver.quit()
