Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch3 p25

---
# Django's workflow
1. An HTTP request comes in from the user, requesting a URL from our site.
2. Django uses logic defined by us to decide which *view* function should deal with the request—this is known as *resolving the URL*.
3. The *view* function processes the request and returns an HTTP response.