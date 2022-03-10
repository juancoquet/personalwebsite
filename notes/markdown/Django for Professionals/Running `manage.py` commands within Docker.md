Note Type: #litnote
Source: [[📖 Django for Professionals]] ch2 p27

---
# Running `manage.py` commands within Docker
When using a Docker container, you should not run `manage.py` commands the usual way as this executes them locally. Instead, any commands should be prefaced with `docker-compose exec {service}`, where `{service}` represents the name of the service (container) in which you wish to run the command. For example, if we have a `web` service defined in our `docker-compose.yml` file, we can create a new Django superuser in this container with the following command:
```bash
$ docker-compose exec web python manage.py createsuperuser
```