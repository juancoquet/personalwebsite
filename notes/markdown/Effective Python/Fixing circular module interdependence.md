Note type: #litnote
Source: [[📖 Effective Python]] item 88

---
# Fixing circular module interdependence
The best way to fix module interdependence that causes the program to crash on startup is to refactor any mutual dependencies into a separate module at the bottom of the dependency tree, that each module can import from.