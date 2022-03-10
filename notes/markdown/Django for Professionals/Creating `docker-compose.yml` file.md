Note Type: #litnote
Source: [[📖 Django for Professionals]] ch1 p20

---
# Creating `docker-compose.yml` file
The compose file is responsible for running a container based on an image. It is a YAML file, which is essentially a JSON-like dictionary-based file type.
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
```

First we specify `version`, which version of Docker Compose to use.

The `services` key contains the containers we want within our Docker host — in this case, we create a `web` container but you might have a separate container for a database or anything else that your app may need.

We tell Docker to look in the current directory for the `Dockerfile` with the `.` next to build. Then we specify a command to run, telling Docker to start our Django server (our source code exists inside the `code` directory as set up in [[Building a Docker image]]).

The `volumes` key tells Docker to sync its filesystem with our local computer's filesystem — we are telling it to look in the current directory `.` and sync it to `/code`. This means that we don't have to rebuild the image with every change to a file, as changes will automatically sync to our container. This works in a bi-directional way, so any changes that happen inside Docker will also be synced to our local filesystem. The leading `-` is just syntax for starting a list of items.

Finally we tell Docker to use port 8000, which is the Django default.

