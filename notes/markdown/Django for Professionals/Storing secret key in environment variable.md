Note Type: #litnote
Source: [[📖 Django for Professionals]] ch8 p127

---
# Storing secret key in environment variable
To hide the Django secret key, it should be put into an environment variable. We can do this by installing the `environs` package as follows:
```bash
$ docker-compose exec {service_name} pipenv install 'environs[django]==8.0.0'
$ docker-compose down
$ docker-compose up -d --buld
```

Next we add the following lines to the top of `settings.py`:
```python
# settings.py

from pathlib import Path
from environs import Env

env = Env()
env.read_env()

...
```

Then we copy the secret key and put it into the `environment` key in `docker-compose.yml`
```YAML
# docker-compose.yml

...

services:
	web:
		...
		environment:
			="DJANGO_SECRET_KEY=fzxv+hlq2me@mf(1uw(7efxhx@hh7a4mov#q^(5\*qs=gh37f7c"
```

One thing to be aware of is that if your secret key includes a `$` character, it should be doubled up `$$`, otherwise you will see an error.

Finally we replace `SECRET_KEY` in `settings.py` to import the environment variable.
```python
# settings.py

...

SECRET_KEY = env("DJANGO_SECRET_KEY")

...
```