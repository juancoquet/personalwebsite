Note Type: #litnote
Source: [[📖 Django for Professionals]] ch11 p167

---
# Displaying inline relational fields in admin
When we have a foreign key relation between tables, we can display related fields by making some changes to the `admin.py` file inside our app. We'll continue working with the model structure laid out in [[Creating a foreign key link in Django]]
```python
# admin.py

from django.contrib import admin
from .models import Book, Review


class ReviewInline(admin.TabularInline):
	model = Review
	
	
class BookAdmin(admin.ModelAdmin):
	inlines = [
		ReviewInline,
	]
	list_display = ("title", "author", "price",)
	

admin.site.register(Book, BookAdmin)
```

We create a `TabularInline` class for our `Review` model, and then tell the `BookAdmin` class to display `ReviewInline`.