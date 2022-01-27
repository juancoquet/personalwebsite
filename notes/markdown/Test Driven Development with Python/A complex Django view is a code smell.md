Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch14 p235

---
# A complex Django view is a code smell
If a view becomes complex, you should think about if there is a different, better way of implementing the logic it contains. Could it be moved to a form? Could it be moved to custom methods inside the model? Maybe even to a non-Django module.