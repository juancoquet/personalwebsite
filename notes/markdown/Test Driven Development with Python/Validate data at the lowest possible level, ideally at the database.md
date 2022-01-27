Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch13 p234

---
# Validate data at the lowest possible level, ideally at the database
Data validation should be handled at the lowest possible level to ensure reliability and security. Validating input data at the database level (using `views.py` and `models.py`), rather than at the forms level ensures that your data remains valid and consistent no matter how complex the code above becomes.