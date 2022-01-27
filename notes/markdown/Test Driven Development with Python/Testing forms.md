Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch14 p237

---
# Testing forms
We can test that forms are being created the way we want by checking if desired attributes exist in the form's HTML when we call `as_p()` on it. If we want to test the `ItemForm` from [[Creating Django ModelForms]], we can do so in the following manner:
```python
# test_forms.py
from django.test import TestCase

from my_app.forms import ItemForm


class ItemFormTest(TestCase):
	
	def test_html_attributes(self):
		form = ItemForm()
		self.assertIn('placeholder="Enter an item"', form.as_p())
		self.assertIn('class="form-control input-lg"', form.as_p())
```

We can also test sending data to a form by providing a `data` argument upon creating the form as a dictionary containing the form fields to which we want to post data.
```python
# test_forms.py
...

class ItemFormTest(TestCase):
	
	...
	
	def test_data_sent_to_form(self):
		form = ItemForm(data={'text': ''})
		self.assertFalse(form.is_valid())
		self.assertEqual(
			form.errors['text'],
			["You can't have an empty list item"]
		)
```

Here we test that trying to send and empty string raises an error which displays the text "You can't have an empty list item". Calling `is_valid()` on the form returns `True` or `False`, validates the input data and populates the `errors` attribute which we then access with `form.errors`. The `errors` attribute being accessed is a dictionary that maps the names of the form's fields to any errors for those fields upon validation. Note that the errors are stored as a list as there could be multiple errors, so when using `assertEqual` be sure to place the error message inside square brackets as shown.