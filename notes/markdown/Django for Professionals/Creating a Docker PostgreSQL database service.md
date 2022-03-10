Note Type: #litnote
Source: [[📖 Django for Professionals]] ch2 p29

---
# Creating a Docker PostgreSQL database service
We can create a designated container for our database by assigning it a `service` in our `docker-compose.yml` file. The below `compose` file creates a service for the Django server and another for the database.
```YAML
# docker-compose.yml

version: '3.8'

services:
	web:
		build: .
		command: python /code/manage.py runserver 0.0.0.0:8000
		volumes:
			- .:/code
		ports:
			- 8000:8000
		depends_on:
			- db
	db:
		image: postgres:11
		environment:
			- "POSTGRES_HOST_AUTH_METHOD=trust"
```

First we create the `web` service (see [[Creating `docker-compose.yml` file]] for explanations), but we add a `depends_on` key to tell Docker that the `web` service depends on the `db` service, meaning that `db` will be started up before `web`.

For our `db` service, we use the `postgres` image pinned to version 11. If no version is specified then the latest version will be selected, but it's a good idea to always pin a specific version to ensure that the container remains the same every time.

We then set up the environment variable `POSTGRES_HOST_AUTH_METHOD=trust` with the `environment` key. This allows us to connect without a password, which is a convenient step to take for development.

When `docker-compose up` is ran, it will create two containers — one for our `web` service and one for our `db` service.