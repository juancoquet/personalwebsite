Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch14 p 239

---
# Creating Django ModelForms
Django comes with a built-in `ModelForm` class that can be used to take and validate user input to match the format of an existing model. It automatically generates HTML if you call `as_p()` on the form from inside the template.
```python
from django import forms

from my_app.models import Item

class ItemForm(forms.ModelForm):
	
	class Meta:
		model = Item
		fields = ('text',)
		widgets = {
			'text': forms.fields.TextInput(attrs={
				'placehorlder': 'Enter an item',
				'class': 'form-control input-lg'
			}),
		}
		error_messages = {
			'text': {'required': "You can't have an empty list item"}
		}
```

Inside the `ModelForm` inheritance class, we define a class `Meta` which is responsible for storing the information about the model the form should use. The `model` attribute points to the model, while the `fields` attribute contains the fields of the chosen model that we want the form to use. 

We can specify a `widgets` attribute to add HTML attributes to each field being used, such as placeholder text and a class name to use with Bootstrap. We can also modify the error messages raised by each field upon unsuccessful data entry. Here, we change the `text` field's `required` message to "You can't...", which will show if the user attempts to pass an empty string to the `text` field in the form.