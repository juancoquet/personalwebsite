Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch5 p59

---
# Testing a POST request
POST requests can be tested by using django's built in test client's `.post` method. It takes a URL pattern argument, to tell the function which page it will attempt to make a POST request on, and a `data` argument which can be passed a dictionary containing the `name` attribute of the HTML element to which you want to post as the key, and your POST data as the value.

For example, say we have the following form in our homepage HTML:
```HTML
<form method="POST">
	{% csrf_token %}
	<input name="item_text" placeholder="Enter item here" />
</form>
```

We can write a unit test for this POST request in the following manner:
```python
from django.test import TestCase:


class MyTest(TestCase):

	def test_home_page_POST_request(self):
		response = self.client.post('/', data={'item_text': 'testing item'})
		self.assertIn('testing item', response.content.decode())
```

The above code creates a `response` object after sending the POST request with the data `'testing item'` into the input field `item_text`, of the form found at the home page (`'/'`). It then checks to see if `'testing item'` can be found in the response's HTML, by calling `reponse.content.decode()` to turn the response into a string of HTML.