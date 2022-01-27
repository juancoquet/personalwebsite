Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch6 p93

---
# Ensure test isolation
It is important to make sure that tests do not affect each other as this can lead to misleading results. You should ensure that each time a test is run, it is run from a blank slate, not picking up the state where a previous test left off.

---
### See also:
- [[Using `LiveServerTestCase` for Django functional tests]]