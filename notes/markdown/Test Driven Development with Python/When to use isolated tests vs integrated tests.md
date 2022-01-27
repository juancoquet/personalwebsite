Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch26 p469

---
# When to use isolated tests vs integrated tests
Applications tend to have different layers — they have the core, internal logic written entirely by the programmer, and *boundaries*, the points at which your code interacts with external systems which you do not control such as the database, external libraries, the web, a file system or a user.

As a general rule, it's a good idea to use isolated tests for the core of the program to help you drive efficient design, and reserve integrated tests (tests that deal with multiple layers of the application) for the boundaries, where the externals that your code has to interact with are not entirely within your control.