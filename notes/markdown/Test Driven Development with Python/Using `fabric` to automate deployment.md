Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch11 p189

---
# Using `fabric` to automate deployment
`fabric` is a python package that can be pip-installed. It can be used to run shell commands with the `run` function as follows:
```python
from fabric.api import run

source_dir = 'home/ubuntu/sites/staging.mysite.com/source'

run(f'mkdir -p {source_dir}/newdir')
```

It also has a `sed` function that allows us to substitute a string in a file:
```python
from fabric.contrib.files import sed


SITENAME = 'juancoquet.com'

path_to_settings = 'my_django_project/settings.py'

# Set DEBUG to False for deployment
sed(path_to_settings, "DEBUG = True", "DEBUG = False")

# Set ALLOWED_HOSTS
sed(path_to_settings, "ALLOWED_HOSTS = []", f'ALLOWED_HOSTS = ["{SITENAME}"]')
```

For deployment, it is good practice to ensure that the `SECRET_KEY` constant in `settings.py` is different on the server than it is on your local repository, as the local repository may be visible by others through github. This can be done in the following manner:
```python
from fabric.contrib.files import append, exists
import random


secret_key_file = 'path/to/secret_key.py'

if not exists(secret_key_file):
	chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
	key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
	append(secret_key_file, f'SECRET_KEY = "{key}"')
append(path_to_settings, '\nfrom .secret_key import SECRET_KEY')
```

We first check if a `secret_key.py` file already exists to see if we have already made a secret key for the server. If it doesn't, we generate a random key and create a file to contain it in a `SECRET_KEY` constant. We use the `SystemRandom()` class from the `random` package to select random characters from `chars` in a cryptographically safe way (the usual `random.choice()` is not safe). Finally, we import `SECRET_KEY` into `settings.py`.

