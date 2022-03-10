Note Type: #litnote
Source: [[📖 Django for Professionals]] ch11 p166

---
# Creating a foreign key link in Django
We'll start with a `Book` model to represent books on our site:
```python
# models.py

from django.db import models


class Book(models.Model):
	title= models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	
```

Now suppose we want to add a `Review` model, so that users can leave reviews for the books they read. This requires a foreign key relation from our `Review` model to our `Book` model.
```python
# models.py

...

class Book(models.Model):
	...
	

class Review(models.Model):
	book = models.ForeignKey(
		Book,
		on_delete=models.CASCADE,
		related_name='reviews'
	)
	review_text = models.CharField(max_length=255)

```

We create a `book` attribute inside the `Review` class and assign it to `models.ForeignKey`, which defaults to a one-to-many relationship.  It is standard practice to name this attribute the same as the model to which it is linking.

The first argument we pass to the `FogerignKey` function is the model to which we are linking, `Book`. We then assign the `CASCADE` behaviour on deletion, meaning that if the `Book` entry to which the review belongs is deleted, so will the review be deleted. Finally we create a `related_name` attribute, which assigns the name by which we can look up related items in a `Book` instance — for example, if we had a book object `my_book`, calling `my_book.reviews` would return all reviews linked to this instance.