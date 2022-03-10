Note type: #litnote
Source: [[📖 Effective Python]] item 87

---
# Dynamic imports
A dynamic import is a way of importing a module to circumvent interdependence issues caused by importing the module at the top of the document as standard. Dynamic imports are done by importing the module within the function that requires the import module's contents. Although this is best avoided, it is often the easiest and quickest way of solving interdependence issues without having to refactor code extensively.