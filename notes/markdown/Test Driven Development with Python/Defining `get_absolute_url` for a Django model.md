Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch13 p233

---
# Defining `get_absolute_url` for a Django model
You can define a special model method in Django called `get_absolute_url` to get the URL of the page that displays the instance of the model it is called on. Assume we have the following model:
```python
# models.py

...

class Item(models.Model):
	
	...
	
	def get_absolute_url(self):
		return reverse('view_item', args=[self.id])
```

This finds the URL associated with the name `'view_item'` and combines it with the ID (or `pk`) of the item it is called on. The method is implicitly called on an object which is passed to `redirect()` as an argument:
```python
# views.py

def some_view(request):
	item = Item.objects.create()
	return redirect(item)
```