Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch7 p128

---
# Testing Django view context items
You can test for the presence of particular context items in the following manner:
```python
from django.tests import TestCase
from my_app.models import TestModel

class MyTest(TestCase):
	
	def test_context_item(self):
		test_item = TestModel.objects.create()
		
		response = self.client.get('some/url/')
		
		self.assertEqual(response.context['context_key'], test_item)
```

`test_item` is the item we are trying to find in the context of the view that is called by `'some/url'`. We can access the context dictionary of the view created the response with the code `response.context['context_key']`, where `'context_key'` is the context item you are testing for.