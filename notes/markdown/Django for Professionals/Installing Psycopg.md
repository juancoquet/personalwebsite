Note Type: #litnote
Source: [[📖 Django for Professionals]] ch2 p33

---
# Installing Psycopg
Installing Psycopg can be easily done through `pipenv`.
```bash
$ pipenv install psycopg2-binary==2.8.5
```

Note that if you want to install it to a docker container (as you should), the above command must be preceded by `docker-compose exec {service_name}`, where `{service_name}` is replaced by the service you wish to install to.
```bash
$ docker-compose exec web pipenv install psycopg2-binary==2.8.5
```

You'll then need to rebuild the image — see [[Rebuild image after installing a package on Docker]]

---
### See also:
- [[Always install new packages within Docker, not locally]]