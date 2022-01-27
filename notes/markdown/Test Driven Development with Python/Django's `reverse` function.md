Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch13 p233

---
# Django's `reverse` function
The `reverse()` function is used to retrieve the URL pattern that pertains to a particular URL name. Suppose you have defined the following URL  in *urls.py*:
```python
url('/foo/', some_view, name='url_name')
```

The name attribute `'url_name'` can be used by both templates (such as using the name instead of hardcoding the URL as a `href` attribute) and by the `reverse()` function. When the `reverse()` function is called with `url_name` as its argument, the URL `'/foo/'` will be returned.This can be used in *views.py* to redirect the user:
```python
# views.py
from django.shortcuts import redirect

def some_view(request):
	...
	

def some_other_view(request):
	...
	return redirect(reverse('url_name'))	# Redirects to /foo/
```

In short, it does the reverse of what Django normally does with *urls.py*—rather than taking a URL and selecting a view, it can go from a view back to a URL.