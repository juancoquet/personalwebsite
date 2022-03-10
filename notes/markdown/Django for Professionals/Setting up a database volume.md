Note Type: #litnote
Source: [[📖 Django for Professionals]] ch3 p40

---
# Setting up a database volume
We can create a volume to sync data in a database service by by specifying a location within the `db` service and a `volumes` that exists outside of the containers.
```YAML
# compose-docker.yml

version: '3.8'

services:
	web:
		...
		depends_on:
			- db
	db:
		image: postgres:11
		volumes:
			- postgres_data:/var/lib/postgresql/data/
		environmnet:
			- "POSTGRES_HOST_METHOD=trust"

volumes:
	postgres_data:
```
