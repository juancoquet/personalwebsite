Note Type: #litnote
Source: [[📖 Django for Professionals]] ch2 p31

---
# Updating `settings.py` to use PostgreSQL
To switch Django's database to use Postgres, the `DATABASES` configuration must be changed in `settings.py`. PostgreSQL requires a name, user, password, host and port to be provided, which are also handled in the `DATABASES` configuration.
```python
# settings.py

...

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'db_name',
		'USER': 'username',
		'PASSWORD': 'userpass',
		'HOST': 'db',
		'PORT': 5432
	}
}

...
```

The `HOST` key is set to `db` which is the name of the Docker service that the database will be running on (see [[Creating a Docker PostgreSQL database service]]). The `PORT` key is set to `5432`, which is the default PostgreSQL port.

*NOTE: this will not yet work, as first a database adapter must be installed — see [[Installing Psycopg]]*