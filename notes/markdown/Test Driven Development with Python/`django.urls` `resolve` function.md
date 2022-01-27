Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch3 p25

---
# `django.urls` `resolve` function
`resolve` is a function that Django uses internally to resolve a URL request and decide which *view* function should be used to handle the request. This is useful for testing purposes, as we can feed `resolve` a URL pattern that we are trying to test and check that we receive the expected *view* function back.
```python
from django.urls import resolve
from my_app.views import home_page

found = resolve('/')	# testing root url, assume we expect a home_page view function back
assertEqual(found.func, home_page)
```