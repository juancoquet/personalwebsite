Note Type: #litnote
Source: [[📖 Django for Professionals]] ch10 p144

---
# Register new models
New apps must be registered with the Django admin to get them to appear at the `/admin` URL. To do this, add the following to the `admin.py` file of your app.
```python
# my_app/admin.py

from django.contrib import admin
from .models import MyModel

admin.site.register(MyModel)
```

We can go one step further and create a `ModelAdmin` sub-class that decides how the `Books` model table will display in the admin site.
```python
# my_app/admin.py

from django.contrib import admin
from .models import MyModel


class MyModelAdmin(models.ModelAdmin):
	list_display = ("attr1", "attr2", "attr3")
	
admin.site.register(MyModel, MyModelAdmin)
```

The admin page will now show the three table columns as specified, in the given order (assume that the `attrX` attributes already belong to `MyModel`).