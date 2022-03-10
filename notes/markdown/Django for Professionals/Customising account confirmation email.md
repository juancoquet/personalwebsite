Note Type: #litnote
Source: [[📖 Django for Professionals]] ch9 p135

---
# Customising account confirmation email
The default email templates can be found in the `django-allauth` Github at `django-allauth/allauth/templates/account/email`. Here you'll find the files `email_confirmation_subject.txt` and `email_confirmation_message.txt`. We can override these in our own project by defining files under the same namespaces, and the same path. In our `templates/account` folder, we create an `email` dub-folder that will contain our email text files.

The text files include several Django template tags, which should be left in, but we can copy copy the contents of the original files and replace the raw text with our custom message. As long as the path matches that of the default flies and the template tags are left in, then it will work.

We can also change the domain name included in the message, which is `example.com` by default. To do this, go to the Django admin and click on the `Sites` section. Here you will see the `example.com` domain name listed — click it and replace it for the domain name of choice.

Finally, we can change the `from` email address (default is `webmaster@localhost`) by adding the following line to `settings.py`:
```python
# settings.py

...

DEFAULT_FROM_EMAIL = 'example@email.com'
```
