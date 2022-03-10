Note Type: #litnote
Source: [[📖 Django for Professionals]] ch6 p85-87

---
# Configuring static files in `settings.py`
There are several configurations we must add or update in `settings.py`.
```python
...

STATIC_URL = '/static/'
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_FINDERS = [
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

...
```

The first is `STATIC_URL`, which is already included. It defines the URL we can use to reference static files. Be sure to include the trailing slash.

Next is `STATICFILES_DIRS`, which defines the location of static files during *local development*. We will set this to be a project-level `static` directory. The syntax looks a little weird — we use `joinpath` to join `BASE_DIR` to `static`, creating`BASE_DIR/static`, and turn the result into a string. The trailing comma is there because there could be future additions where static files might also exist.

`STATIC_ROOT` defines the location of static files for *production*. The typical name for this directory is `staticfiles`. It is better to have all static files in one place for production, which is what `collectstatic` does (see [[Using `collectstatic`]]) — this will gather all static files found in the project inside the directory defined by `STATIC_ROOT`.

The last setting is `STATICFILES_FINDERS`, which is implicitly set by Django but it's not a bad idea to set them explicitly in `settings.py`. It tells Django *how* to look for static file directories — first `FileSystemFinder` looks in `STATICFILES_DIRS` (defined above) for any static files, then `AppDirectoriesFinder` looks for any directories named `static` inside our apps. Order matters here, as only the first file will be kept in the event that two files with matching names are found.