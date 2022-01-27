Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch14 p242

---
# Testing that a form is used in a view
We can test that a form is part of a view by using the testing client to make a GET request to the page in question, and then accessing the `context` attribute of the response.

For example, if we have this home page view:
```python
# views.py
from my_app.forms import ItemForm


def home_page(request):
	return render(request, 'home.html', {'form': ItemForm()})
```

We have given an instance of `ItemForm` the name `'form'` in our context dictionary, which we can access by using the `.context` attribute of our response object in our unit test:
```python
# test_views.py
from django.test import TestCase

from my_app.forms import ItemForm


class HomePageTest(TestCase):
	
	def test_home_page_uses_item_form(self):
		response = self.client.get('/')		# Request home page
		self.assertIsInstance(response.context['form'], ItemForm)
```

We can use `assertIsInstance` to check that the `'form'` key of the response's `context` dictionary maps to an instance of `ItemForm`.

---
### See also:
- [[Testing forms]]