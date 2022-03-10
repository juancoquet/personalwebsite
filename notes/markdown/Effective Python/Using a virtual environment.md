Note type: #litnote
Source: [[📖 Effective Python]] item 83

---
# Using a virtual environment
While inside your virtual environment directory, you need to access the `bin/activate` script to activate the virtual environment.
```
$ source bin/activate
(myproject) $ 
```

The name of the virtual environment will precede the shell prompt `$` to indicate that the virtual environment is now activated. Any required packages must now be installed within this environment as each new environment is a blank slate, even if your system has globally-installed packages.

Deactivating a virtual environment is as simple as using the `deactivate` command.
```
(myproject) $ deactivate
$
```

This will return you to the default global system.

---
#### See also:
- [[Using `venv` to create a virtual environment]]