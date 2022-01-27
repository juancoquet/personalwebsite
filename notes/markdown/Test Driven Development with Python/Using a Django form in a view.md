Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch14 p247

---
# Using a Django form in a view
To use a form as part of a view, you need to pass the `request.POST` data into the form's constructor. You can then validate the the data with `.is_valid()`, and use control flow to determine what happens in successful and unsuccessful submission events.

```python
# views.py
from django.shortcuts import render

from my_app.forms import ItemForm


def my_view(request):
	form = ItemForm(data=request.POST)
	if form.is_valid():
		...
	else:
		...
		
```