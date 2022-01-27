Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch12 p209

---
# Generic explicit wait helper function for testing
When testing using selenium, we often need to find elements on the page for assertions against their content. However, sometimes the page takes a moment to load meaning that we need to wait for the element to appear before our assertion runs. Selenium has some built-in wait methods, but they are not very good. We can build our own generic wait function as follows:
```python
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time


MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
	
	def wait_for(self, fn):		# Takes function as argument
		start = time.time()
		while True:
			try:
				return fn()
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)
```

This `wait_for` method takes a function as an argument—we will feed it a lambda function that executes the assertion we want to test for.
```python

class FunctionalTest(LiveServerTestCase):

	def wait_for(self, fn):
		...
	
	def test_element(self):
		self.wait_for(lambda: self.assertEqual(
			self.browser.find_element_by_id('id_test_element').text,
			"Test works!"
		))
```

The lambda function tries to find the element with ID 'id_test_element' and gets its text. It expects to find "Test works!". If it does find what it expects, it returns `True` and breaks the `while True` loop—otherwise it returns `False` repeatedly with each call around the loop.