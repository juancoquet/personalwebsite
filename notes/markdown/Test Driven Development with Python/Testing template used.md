Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch4 p47

---
# Testing template used
The template used for a specific URL pattern can be tested by using Django's test client. The test client can be used as an attribute of Django's `TestCase` class. It is used to request a URL pattern, and it then uses this URL pattern to find the appropriate *view*. If it finds a *view* for the URL, it executes the view, giving us a response.
```python
from django.test import TestCase


class MyTest(TestCase):
	
	def test_template_used(self):
		response = self.client.get('/')		# Requesting root url
		self.assertTemplateUsed(response, 'home.html')	# checks response template
```

Because the client has to fetch the appropriate *view* for the provided URL, this method also implicitly tests that our URL pattern uses the correct *view*.

---
### See also:
- [[Basic `unittest` example]]