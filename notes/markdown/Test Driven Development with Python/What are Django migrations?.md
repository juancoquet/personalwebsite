Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch6 p68

---
# What are Django migrations?
Django comes with a tool called *migrations* which is responsible for creating, updating and deleting tables and columns in your database. It reads changes made to the `models.py` file inside an app, and translates those changes to the database when `python manage.py makemigrations`and `python manage.py migrate` are called.

`makemigrations` is a kind of staging area for migrations, and `migrate` applies staged changes to the database.

It also acts as a kind of version control for your database, as each migration made is automatically logged.