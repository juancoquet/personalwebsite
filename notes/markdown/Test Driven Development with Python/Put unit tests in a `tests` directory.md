Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch12 p214

---
# Put unit tests in a `tests` directory
For each Django app created, give it a `tests` directory to house all the unit tests for that app. This will make it easier to keep all your test files in one place from the beginning. By including an `__init__.py` file in the `tests` directory, Django will recognise it and run the tests inside when `python manage.py test app_name` is called.

You usually want to test each source code file with a different test file in the `tests` directory, which means that you should end up with `test_models.py`, `test_views.py` and `test_forms.py`