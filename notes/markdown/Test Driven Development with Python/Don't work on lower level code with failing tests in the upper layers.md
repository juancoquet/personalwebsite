Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch23 p401

---
# Don't work on lower level code with failing tests in the upper layers
You should not start working on lower-level (or 'inner') implementations if you have failing tests in the upper layers of code — for example, you should not work on your Django model code if you have tests failing for the views or even the URL layer.

If you have cross-layer dependencies, it means that your tests need to be more isolated, they need to test more self-contained problems. This usually means breaking them down into multiple smaller tests, and using mocks if necessary.

---
### See also:
- [[Outside-In testing]]