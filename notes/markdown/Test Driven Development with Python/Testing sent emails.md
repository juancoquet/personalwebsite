Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch18 p314

---
# Testing sent emails
When we are running tests, Django allows us to see any emails that the server tries to send by accessing the `outbox` attribute of `django.core.mail`.
```python
from django.core import mail
from django.test imprt LiveServerTestCase

class email_test(LiveServerTestCase):
	
	def test_email_sent(self):
		email = email_outbox[0]
```

Here we access the first email in the list of emails that the server has tried to send. We can access its target recipient with `email.to`, its subject with `email.subject` and its message body with `email.body`.