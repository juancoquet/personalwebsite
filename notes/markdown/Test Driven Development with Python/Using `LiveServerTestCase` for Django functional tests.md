Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch6 p84

---
# Using `LiveServerTestCase` for Django functional tests
The problem with using `unittest`'s standard `TestCase` class for web development functional tests is that it will use the real database by default. We could use `setUp()` and `tearDown()` methods to clean up after ourselves to avoid littering the database every time we run a test but it's better to use `LiveServerTestCase` from `django.test` as it does the work for us—it creates a temporary database and a test server.

`LiveServerTestCase` expects to be run by `manage.py`, and it will run any files whose names begin with `test`. It will look inside any python packages, so it's important to make sure the directory in which your functional test files are stored has an `__init__.py` file.

In short, make a `functional_tests` directory, create an `__init__.py` file inside it and make your functional test classes inherit from `django.test.LiveServerTestCase`.

---
### See also:
- [[Functional tests]]