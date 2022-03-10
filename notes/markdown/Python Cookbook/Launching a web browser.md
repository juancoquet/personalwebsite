Note type: #litnote
Source: [[📖 Python Cookbook]] ch13.15 p563

---
# Launching a web browser
A web browser can easily be launched with the `webbrowser` module.
```python
import webbrowser

webbrowser.open('http://www.runescape.com')		# Opens in default browser
```

More specific behaviours can also be defined.
```python
webbrowser.open_new('http://www.runescape.com')			# Opens in new window
webbrowser.open_new_tab('http://www.runescape.com')		# Opens new tab

firefox = webbrowser.get('firefox')						# Use specific browser
firefox.open('http://www.runescape.com')
```

This is a quick and easy way to launch a browser. For more advanced browser usage, see [Selenium](https://selenium-python.readthedocs.io/).