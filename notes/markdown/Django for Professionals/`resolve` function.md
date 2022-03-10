Note Type: #litnote
Source: [[📖 Django for Professionals]] ch4 p62, https://docs.djangoproject.com/en/3.2/ref/urlresolvers/

---
# `resolve` function
The `resolve` function is used to get the view that a URL pattern invokes.
```python
from django.urls import resolve

from .views import home_page


view = resolve('/')
assertEqual(view.func, home_page)
```

The `resolve` function returns a `ResolverMatch` object, which allows you to access data about the resolved URL. One of these data is `.func`, which contains the view function that would be used to serve the URL. It also has `.args` and `.kwargs`, which contain the arguments that would be passed to the view function, as parsed from the URL.

See https://docs.djangoproject.com/en/3.2/ref/urlresolvers/ for more.