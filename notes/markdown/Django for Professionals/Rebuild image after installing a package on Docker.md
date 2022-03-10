Note Type: #litnote
Source: [[📖 Django for Professionals]] ch2 p33

---
# Rebuild image after installing a package on Docker
After installing a new package on Docker, the image must be re-built to force Docker to use the new `Pipfile` and `Pipfile.lock`. To do this, first stop active containers and then run the `docker-compose up -d` command again with the `--build` flag.
```bash
$ docker-compose down
$ docker-compose up -d --build
```