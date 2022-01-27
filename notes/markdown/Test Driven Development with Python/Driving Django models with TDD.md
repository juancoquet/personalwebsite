Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch18 p320

---
# Driving Django models with TDD
Driving the creation of Django models with TDD can be annoying because it involves the extra step of having to make migrations before you can test the changes you make to your model. After creating your unit test, the cycle follows the tune of running the test, reading the error,  making a minimal code change, deleting old migrations, running `makemigrations`, running the test, reading the error... and so on, until the test passes.