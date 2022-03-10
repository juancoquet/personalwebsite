Note Type: #litnote
Source: [[📖 Django for Professionals]] ch6 p88

---
# Loading static files into templates
To load static files into our templates, first use the `{% load static %}` template tag at the top of the HTML document. This imports the directory defined by `STATIC_URL` (see [[Configuring static files in `settings.py`]]), in our case called `static`, inside which we have three directories — `css`, `js` and `images`.

We then load in static files by referencing their path relative to the `static` directory we loaded above. For example, to load our `base.css`, we include the following code in the document's `<head>`.
```HTML
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Page Title</title>
	
	<!-- CSS IMPORTED HERE -->
	<link rel="stylesheet" href="{% static 'css/base.css'}">
</head>

...
```

Shown above is loading a CSS stylesheet, but the same method applies to any type of static file, like images and JavaScript — first use the `{% load static %}` template tag at the top of the document, then use the `{% static 'sub_folder/file' %}` syntax. Below are examples loading an image and JavaScript:
```
{% load static %}

...

<img src="{% static 'images/my_image.png' %}">

<script src="{% static 'js/my_script.js' %}"></script>

```
