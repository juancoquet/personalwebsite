Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch20 p361

---
# How do Django sessions work?
Servers need a way of recognising different clients with every single request. To do this, it assigns each client a session ID, stored in a cookie, which is sent with every request to the server. The server stores that ID in the database by default, and it uses these stored session IDs to recognise different clients. Every visitor to the site is given a session ID, whether they are logged in or not.

If we want to recognise a client as being logged in and authenticated, the server can mark the client's session (found by using the stored session ID) as being authenticated and associate that session with a user ID — this way, authentication credentials do not have to be sent with every single request.