Note Type: #litnote
Source: [[📖 Django for Professionals]] ch9 p138

---
# Customising email confirmation page
If you look at `django-allauth`'s Github repository, you'll see that the default email template exists at `templates/account/email_confirm.html`. If we shadow this namespace within our own project, we can copy the boilerplate to our project override the default page with whatever we choose.
```bash
$ touch templates/account/email_confirm.html
```

```HTML
<!-- templates/account/email_confirm.html -->
{% extends "my_base.html" %}	<!-- NEW: extend our own base page -->

{% load i18n %}

{% load account %}

...
```