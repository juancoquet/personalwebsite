Note type: #litnote
Source:  [[📖 Test Driven Development with Python]] ch1 p5

---
# First Django web app test
The first test you should write when building a new Django web app should be to test that the Django server is set up. This can be done as follows:
```python
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
```

Of course, this assumes that Selenium is already installed in the virtual environment.