Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch6 p85

---
# Accessing `LiveServerTestCase` server with selenium
To access our page using selenium for our functional tests, we can't hard code the `localhost` URL to our `browser.get()` function. Instead, we can use the `LiveServerTestCase` attribute `live_server_url`:
```python
from django.test import LiveServerTestCase
from selenium import webdriver


class FuncTests(LiveServerTestCase):

	def setUp(self)
	self.browser = webdreiver.Firefox()
	
	def testing(self):
		self.browser.get(self.liveserverurl)
```

---
### See also:
- [[Using `LiveServerTestCase` for Django functional tests]]