Note Type: #litnote
Source: [[📖 Django for Professionals]] ch3 p40

---
# What are Docker volumes?
Docker volumes allow you to sync data bidirectionally between a container and your local computer — any changes to either local files or container files will show up in both. They are set up in the `docker-compose.yml` file, by specifying a `volumes` key and mapping a local directory to a docker directory.
```YAML
# docker-compose.yml

version:'3.8'

services:
	web:
		build: .
		command: python /code/manage.py runserver 0.0.0.0:8000
		volumes:
			- .:/code
		ports:
			...
		...
```

In the above code, we sync the local directory where the `compose` file exists to the `/code` directory in the Docker container using `.:/code`. The leading `-` is syntax to represent a list item, so we could create another volume with another line below this one starting with a `-`. The `.` represents the local directory where the `compose` file is stored.