Note type: #litnote
Source: [[📖 Effective Python]] item 83

---
# Recreating dependencies with `freeze`
If you need to transfer a project elsewhere, such as a server in a database or another workstation, all dependencies will need to be available on the destination system in order to successfully use the project—all required packages need to be installed. This is made easy with the `pip freeze` command, which will write all dependencies to a file which is called `requirements.txt` by convention.
```
(myproject) $ python3 -m pip freeze > requirements.txt
(myproject) $ cat requirements.txt
numpy==1.16.2
requests==2.21.0
urllib3==1.24.1
```

This file can then be used in another virtual environment to install all required dependencies by using `-m pip install -r` on the `requirements.txt` file inside the new virtual environment.
```
(otherproject) $ python3 -m pip install -r requirements.txt
(otherproject) $ python3 -m pip list
numpy==1.16.2
requests==2.21.0
urllib3==1.24.1
```

---
#### See also:
- [[Do not install packages globally]]
- [[Using `venv` to create a virtual environment]]