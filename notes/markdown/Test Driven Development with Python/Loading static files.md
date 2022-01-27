Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch8 p144

---
# Loading static files
To get Django to load static files, they must first be placed inside a directory named 'static' within inside one of our app directories. By default, Django looks for a 'static' directory inside each app, and it is instructed by `settings.py` to look for this directory when a URL begins with `'/static/'`:
```python
# settings.py
...

STATIC_URL = '/static/'

...
```

Once this is set up, we must configure the link to our stylesheet in the head of our bootstrap implementation to tell Django where to find the appropriate file. The link should begin with `'/static/'`.
```HTML
<!-- base.html -->

<head>
	...
	<!-- Path to stylesheet -->
	<link href="/static/bootstrap/css/bootstrap.min.css" rel="stylesheet">
	...
</head>
```

When Django sees this request, it knows to look for a static file because it begins with `'/static/'`. It then goes through each app directory in our project and looks for a file that matches the path provided, in this case `'/bootstrat/css/...'`.