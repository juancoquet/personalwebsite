Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch9 p158

---
# Setting up a staging server for tests
In order to begin the deployment process, it's best to have a staging server where we can see how our site will behave before pushing to the live server. This gives us a layer in between the final deployment server and our local computer, as the staging server is a remote server which gives us the ability to do a kind of 'soft' deployment.

To set up a staging server for testing purposes, first save the URL where the server will be in an environment variable called `STAGING_SERVER`. Once this is done we can replace the `StaticLiveServerTestCase`'s (or `LiveServerTestCase`) `.live_server_url` attribute to our `STAGING_SERVER` variable inside the `setUp()` method.
```python
import os
from django.tests import StaticLiveServerTestCase
from selenium import webdriver


class MyTest(StaticLiveServerTest):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		staging_server = os.environ.get('STAGING_SERVER')
		if staging_server:
			self.live_server_url = f'http://{staging_server}'
```

This is a hacky approach that will override the default server URL that `LiveServerTestCase` uses. The `if` clause allows us to still run tests normally if a `STAGING_SERVER` variable has not been defined.

You can run these tests using the staging server by defining the variable before the test command in the shell:
```bash
$ STAGING_SERVER=my-staging-url.co.uk python manage.py test
```