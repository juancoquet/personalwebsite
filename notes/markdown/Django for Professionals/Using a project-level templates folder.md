Note Type: #litnote
Source: [[📖 Django for Professionals]] ch4 p51

---
# Using a project-level templates folder
By default, Django looks for a `templates` folder inside each app. It is easier to manage you templates if they are kept in one place, a project-level folder. You can do this by updating `TEMPLATES` in `settings.py`.
```python
# settings.py

...

TEMPLATES = [
	{
		...
		'DIRS':[str(BASE_DIR.joinpath('templates'))],
		...
	}
]

...
```

We are telling Django to append join `templates` to the `BASE_DIR` (`BASE_DIR/templates`, and to look for template files in that folder.

Updating `DIRS` means that Django will look for templates in the specified path *as well as*, not instead of, a local app `templates` folder.