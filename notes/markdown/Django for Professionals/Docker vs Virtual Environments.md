Note Type: #litnote
Source: [[📖 Django for Professionals]] ch1 p8

---
# Docker vs Virtual Environments
The difference between Docker and python virtual environments is that Docker containers are a much more fundamental virtualisation. Virtual environments only isolate Python packages. They do not isolate non-Python software like a PostgreSQL or MySQL database. They also rely on a global installation of Python on your machine — the virtual environment just points to the global installation, it doesn't contain the Python installation itself.

A container goes further, as it isolates the entire OS, not just the Python packages. This means that you must install Python within your docker container, as well as your production-level database.