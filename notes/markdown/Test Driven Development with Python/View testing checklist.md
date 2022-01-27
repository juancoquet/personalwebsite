Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch15 p274

---
# View testing checklist
1. Make sure to use the Django test client (see [[Testing template used]] for more info on the test client)
2. Test that the template used is what you expect.
3. Test each item in the view context dictionary.
4. Test that each form (also accessed through the context dictionary) is the expected class.
5. Test template logic—`for` and `if` statements might deserve testing.
6. Test both valid and invalid occurrences of POST requests.
7. Test that forms are rendered and error messages displayed.