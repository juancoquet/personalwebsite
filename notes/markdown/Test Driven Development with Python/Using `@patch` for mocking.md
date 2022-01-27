Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch19 p330

---
# Using `@patch` for mocking
We can use the `@patch` decorator from `unittest.mock` to simplify the mocking process. We set up a manual mock in [[Mocking sending an email]], now we will use `@patch` to achieve the same thing but with less code.
```python
# test_views.py

from django.test import TestCase
from unittest.mock import patch

import views

EXPECTED_SUBJECT = '...'
EXPECTED_BODY = '...'
EXPECTED_FROM_EMAIL = '...@....com'


class EmailTest(TestCase):

	@patch('views.send_mail')
	def test_sends_mail_to_address_from_POST(self, mock_send_mail):		
		self.client.post('/url_invokes_send_confirmation_email', data={
			'email' = 'abc123@example.com'
		})
		
		self.assertTrue(mock_send_mail.called)
		(subject, body, from_email, to_email_list), kwargs =
			mock_send_mail.call_args
			
		self.assertEqual(subject, EXPECTED_SUBJECT)
		self.assertEqual(body, EXPECTED_BODY)
		self.assertEqual(from_email, EXPECTED_FROM_EMAIL)
		self.assertEqual(to_email_list, ['abc123@example.com'])
```

The `@patch` decorator takes the dot-notated name of an object as a string, and it patches this as a Mock object. We then feed this Mock object into the test method as the `mock_send_mail` argument — this can be named whatever you want, but it's a good convention to name it `mock` followed by the name of the object which it is mocking.

We then execute the code that calls the `send_mail` function, except that thanks to the `@patch` decorator it's actually the patched Mock object that is being called. We can then make assertions on the Mock object, such as checking that it was called. We call `mock_send_mail.call_args` after verifying that the Mock object was called to extract the arguments which it was called with, and finally we compare these arguments to those we expected.

As well as mocking a function, the `@patch` decorator can also be used to mock an entire module. When this is done, all the objects inside the module also become mocks.

---
### See also:
- [[What is a Mock object?]]