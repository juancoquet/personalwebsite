Note Type: #litnote
Source: [[📖 Django for Professionals]] ch6 p99

---
# Using crispy forms
Crispy forms is a third-party package for improving the look of Django forms. To install, `pip install django-crispy-forms` — remember to install within your Docker container if using Docker.

Next we must include it in `INSTALLED_APPS` inside `settings.py`, by adding `crispy_forms` to the list. We must also set the below constant inside `settings.py` when using with Bootstrap:
`CRISPY_TEMPLATE_PACK = 'bootstrap4'`

The final step is to implement crispy forms in the template where your form is being presented. First use a `load` tag to load crispy forms tags, then use the syntax `{{ form|crispy }}`, assuming that the view has included the form under the name 'form' in the context dictionary.
```HTML
{% extends 'base.html' %}
{% load crispy_forms_tags %}

...

<form method="post">
	{% csrf_token %}
	{{ form|crispy }}
	<button type="submit">Submit</button>
</form>
```