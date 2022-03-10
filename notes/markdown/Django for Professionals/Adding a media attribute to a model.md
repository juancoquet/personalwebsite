Note Type: #litnote
Source: [[📖 Django for Professionals]] ch12 p177

---
# Adding a media attribute to a model
We can add media attributes to models by using the field types `ImageField` and `FileField`. Before we do this, we need to make sure that we follow the steps in [[Configuring Django for media uploads]] for it to work.
```python
# models.py

...


class MyModel(models.Model):
	image = models.ImageField(upload_to='images/')

```

The `upload_to` argument tells Django where to save the uploaded image. In this case, it will save it to `MEDIA_ROOT/images/` — `MEDIA_ROOT` is implicit, it is set up in the preliminary configuration steps. The directory `images` must also be created in the filesystem prior to this step.

Be sure to run `makemigrations` and `migrate` after updating your model.

After adding this to the model, the media is accessible to templates by using `{{ model_instance.image.url }}`.