Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch8 p149

---
# Using `collectstatic`
Django helpfully finds static files across our apps, but we want to change that behaviour when we deploy as it is rather slow. To do that, we must collect all the static files in one place where the deployment server can find them—this is what `collectstatic` is for.

It is best to create a new `static` directory at the workspace level, outside of the project. We can then tell Django that this is where the server should look for the static files, by defining `STATIC_ROOT` in `settings.py`.
```python
# settings.py

...

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../static'))
```

Here we are telling Django that the `STATIC_ROOT` directory can be found at `BASE_DIR/../static/`—`BASE_DIR` is a constant that is automatically defined by Django as the base directory of the project (the directory that contains `manage.py`).