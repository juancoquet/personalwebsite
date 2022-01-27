Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch23 p416

---
# Use helper methods to keep ORM calls in the model layer
Django's ORM provides a nicer interface than raw SQL, but it can still get cumbersome if we repeatedly execute ORM calls in our views and forms. To remedy this, we can create helper methods in the model layer and give them descriptive names that we can call in the upper views and forms layers, making our code more legible and easier to test.