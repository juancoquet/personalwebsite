Note type: #litnote
Source: [[📖 Python Cookbook]] ch13.4 p544

---
# Prompting for user password at runtime
To ask for the current user's password at runtime in the terminal, use the `getpass` module.
```python
import getpass

user = getpass.getuser()		# Automatically gets active user
passwd = getpass.getuser()		# Prompts for a password


if authenticate(user, passwd):		# First define this function
	print('Success!')
else:
	print('Incorrect password.')
```

The first thing to note is that the `authenticate` function has to be defined—this is just a pseudo-code example. The function may be defined to compare the input user and password to predetermined environment variables or something of the sort.

Upon runtime the console will prompt for a password where the input characters are not visible.