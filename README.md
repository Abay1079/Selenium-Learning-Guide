# Selenium Learning Guide 🚀

A beginner-friendly guide to learning **Selenium with Python** — covering setup, core concepts, hands-on examples, and curated video tutorials.

---

## 📌 About
This repository is a structured roadmap and resource hub for learning **Selenium WebDriver** in Python.  
It’s designed for:
- Beginners who know basic **Python** but are new to Selenium.
- Learners who want both **theory** and **hands-on practice**.
- Developers looking for a **quick reference** on Selenium basics.

---

## 📖 Contents
1. **Setup & Installation**
   - Python & pip
   - Install Selenium:  
     ```bash
     pip install selenium
     ```
   - Download the correct browser driver (e.g. [ChromeDriver](https://chromedriver.chromium.org/)).

2. **First Script**
   ```python
   from selenium import webdriver

   driver = webdriver.Chrome()
   driver.get("https://www.google.com")

   print(driver.title)
   driver.quit()
