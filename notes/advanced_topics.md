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
