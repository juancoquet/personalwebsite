Note Type: #litnote
Source: [[📖 Django for Professionals]] ch12 p176

---
# Configuring Django for media uploads
In order to safely accept media uploads (see [[Static files vs media files]]), we need to instantiate several configurations. We'll begin with the following in `settings.py`:
```python
# settings.py

...

MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR.joinpath('media'))

```

`MEDIA_ROOT` is the absolute filesystem path to the directory for user-uploaded files, and `MEDIA_URL` is the URL we can use in out templates to access these files. Be sure to make both of these changes after the definition of the `STATICFILES_FINDERS` constant which appears near the bottom of `settings.py`.

Next we made the `media` directory we just told `settings.py` to expect at the project level.
```bash
$ mkdir media
```

For Django to be able to handle images, we must have `pillow` installed.
```bash
$ docker-compose exec {service_name} pipenv install pillow==7.2.0
$ docker-compose down
$ docker-compse up -d --build
```

The final configuration is for us to be able to see media items locally — since media files are assumed to exist in production (they are uploaded by users), we need a way to see them in the development environment. To do this, we add the following configurations in the project-level `urls.py` file:
```python
# urls.py

from django.conf import settings
from django.conf.urls.static imort static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	...
	# Your url patterns
	...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
