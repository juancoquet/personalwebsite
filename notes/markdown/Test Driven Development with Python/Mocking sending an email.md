Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch19 p325

---
# Mocking sending an email
An email sending function can be mocked for testing so that you can test that it's working properly without actually having to send an email. To do this, a kind of 'proxy' of the function has to be defined that stores the email information rather than sends it. Say we have a function in `views.py` that sends an email to a user:
```python
# views.py
# pseudo-code
from django.core.email import send_mail

def send_confirmation_email(request):
	email = request.POST['email']	# gets email address provided by user
	send_mail(
		email.subject,
		email.body,
		email.from,
		email.to
	)
```

We can test that this function works as intended — that it receives the appropriate data from the POST request — by creating a function inside of our test method that stores the values it receives from the post request within class attributes, and then overriding the original `send_confirmation_email` function with out proxy function for the test.
```python
# test_views.py

from django.test import TestCase
import views

EXPECTED_SUBJECT = '...'
EXPECTED_BODY = '...'
EXPECTED_FROM_EMAIL = '...@....com'

class EmailTest(TestCase):

	def test_sends_mail_to_address_from_POST(self):
		self.send_mail_called = False	# check original func called
		
		def fake_send_mail(subject, body, from_email, to_email_list) # proxy
			self.send_mail_called = True
			self.subject = subject
			self.body = body
			self.from_email = from_email
			self.to_email = to_email_list
			
		views.send_mail = fake_send_mail	# override
		
		self.client.post('/url_invokes_send_confirmation_email', data={
			'email' = 'abc123@example.com'
		})
		
		self.assertTrue(self.send_mail_called)
		self.assertEqual(self.subject, EXPECTED_SUBJECT)
		self.assertEqual(self.body, EXPECTED_BODY)
		self.assertEqual(self.from_email, EXPECTED_FROM_EMAIL)
		self.assertEqual(self.to_email_list, ['abc123@example.com'])
```

The `fake_send_mail` function receives the same arguments (in the same order) as the `send_mail` function, which means that when we do the override by reassigning the `views.send_mail` function we can then use whatever arguments were passed to `send_mail` for testing purposes. Remember to do this reassignment *before* executing the code that calls `send_mail`, otherwise the mocking will not work as the arguments will not be passed to the proxy function. We store the arguments in `self.subject`, `self.body` etc., for comparison assertions later.

We execute a POST request on the URL that invokes the `send_confirmation_email` view, and finally we compare the arguments that our `fake_send_mail` function received with the values that we expected to check that our application is working as it should.