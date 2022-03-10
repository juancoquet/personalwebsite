Note type: #litnote
Source: [[📖 Effective Python]] Item 83

---
# Do not install packages globally
Installing packages globally (not inside a virtual environment) can lead to problems due to dependencies across packages. It seems like if you don't import a package into an existing project then it shouldn't interfere with anything, however, the packages that you *do* import into your projects each have their own dependencies on other packages. This can lead to obscure errors if you have many global packages installed, so it's best to only install packages inside virtual environments.