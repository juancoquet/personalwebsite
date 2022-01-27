Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch20 p366

---
# Creating a `@wait` decorator
We can use a decorator to abstract away much of our waiting implementation (waiting for elements to load during tests).
```python
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time


MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):
	
	def wait(self, fn):
		def modified_fn(*args, **kwargs):
			start_time = time.time()
			while True:
				try:
					return fn(*args, **kwargs)
				except (AssertionError, WebDriverException) as e:
					if time.time() - start_time > MAX_WAIT:
						raise e
					else:
						time.sleep(0.5)
		return modified_fn
```

We can now use this decorator to wrap any function that has to wait for an element to load:
```python
...

class FunctionalTest(StaticServerTestCase):

	def wait(self, fn):
		...
	
	@wait
	def wait_for_element(self, element_id):
		self.browser.find_element_by_id(element_id)		
```

---
### See also:
- [[Generic explicit wait helper function for testing]]