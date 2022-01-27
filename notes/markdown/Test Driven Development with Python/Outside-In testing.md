Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch22 p400

---
# Outside-In testing
Outside-In testing is a subset of test-driven development — it is when you begin by writing functional tests for the outer most layers of your program, the user interface, and work your way in towards the innermost implementation dependencies, writing tests along the way.

The way this looks when working with Django is to begin by writing a functional test for some part of the front end of the website that the user will interact with, then proceed to the URL layer (`urls.py`), then the template layer (writing the HTML for the page), then the view layer, and finally the model layer. The key thing to remember is to always write unit tests as you go, before you write any production code. Always test, then implement.