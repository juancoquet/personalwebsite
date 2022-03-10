Note Type: #litnote
Source: [[📖 Django for Professionals]] ch2 p30

---
# PostgreSQL database is not file-based
Unlike the default Django `sqlite3` database, PostgreSQL is not file-based so data will not be maintained when `docker-compose down` is executed. To avoid data from being lost, a `volumes` mount must be added to the database service in side the `docker-compose.yml` file.