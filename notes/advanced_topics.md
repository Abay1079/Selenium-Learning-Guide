# Advanced Selenium Topics

This guide covers more complex scenarios when working with Selenium in Python.

---

## 1. Handling Multiple Windows / Tabs
Sometimes clicking a link opens a new tab or window.

```python
driver.find_element(By.LINK_TEXT, "Open new tab").click()

# Switch to the new tab
windows = driver.window_handles
driver.switch_to.window(windows[-1])
```

---

## 2. Working with Iframes
Web pages often embed content inside iframes.

```python
# Switch into iframe by name/id
driver.switch_to.frame("frameName")

# Or by index
driver.switch_to.frame(0)

# Go back to the main page
driver.switch_to.default_content()
```

---

## 3. Handling Alerts and Pop-ups
Deal with JavaScript alert/confirm dialogs.
```python
alert = driver.switch_to.alert
print(alert.text)
alert.accept()   # Click OK
# alert.dismiss() # Click Cancel
```

---

## 4. Executing JavaScript
Sometimes elements are hidden or not directly interactable.

```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

element = driver.find_element(By.ID, "hiddenButton")
driver.execute_script("arguments[0].click();", element)
```

---

## 5. Taking Screenshots
Useful for debugging or reports.
```python
driver.save_screenshot("screenshot.png")
```

---

## 6. File Uploads and Downloads
Upload
```python
upload_box = driver.find_element(By.ID, "fileInput")
upload_box.send_keys("C:\\path\\to\\file.txt")
```
Download
```python
Configure browser options (example with Chrome):

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": "C:\\Downloads"
})
driver = webdriver.Chrome(options=options)
```

---

## 7. Headless Mode
Run browser without GUI (faster, for automation servers).
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
```

---

## 8. Page Object Model (POM)
For larger projects, use POM to organize your code.
```python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "submit").click()
```
POM makes your code more reusable and maintainable.

---

## 9. Integration with Testing Frameworks
Combine Selenium with testing tools:

- unittest (Python built-in)
- pytest (popular, flexible)
- robotframework (keyword-driven)

Example with pytest:

```python
def test_google_title():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    assert "Google" in driver.title
    driver.quit()
```

---

## 10. Tips for Stability

- Prefer explicit waits over time.sleep().
- Use unique locators (IDs > XPath).
- Handle dynamic content carefully.
- Keep drivers up to date.

---

👉 This file gives learners **everything they need to go beyond basics**: multiple windows, iframes, alerts, headless mode, POM, testing frameworks.  

Do you also want me to make a **matching advanced example script** (e.g. `examples/05_advanced_demo.py`) so people can try these right away?

---
