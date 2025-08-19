# Waits and Timeouts

## Implicit Wait
```python
driver.implicitly_wait(10)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "myElement"))
)
