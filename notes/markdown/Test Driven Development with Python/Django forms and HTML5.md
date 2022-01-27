Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch14 p252

---
# Django forms and HTML5
Django forms automatically add HTML attributes to fields. One of these attributes is the `required` attribute for required fields. In doing so, the browser can validate user input client-side and display an error message if the user attempts to send faulty data.

We can test for the presence of these errors by finding the CSS pseudo-selectors `:valid` and `:invlaid`. For example, if we have a `text` field, the Django form will automatically give it the ID name `id_text` when it creates the HTML for the form. We can find CSS elements with the syntax `#{id_name}:valid` or `#{id_name}:invalid`—in this case, that would be `id_text:valid` and `id_text:invalid`.