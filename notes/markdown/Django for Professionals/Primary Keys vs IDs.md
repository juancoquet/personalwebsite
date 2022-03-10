Note Type: #litnote
Source: [[📖 Django for Professionals]] ch10 p158

---
# Primary Keys vs IDs
Django's `DetailView` treats `pk` and `id` interchangeably, but there is a subtle difference. By default, Django internally adds an automatically incrementing `id` field to every model which is used as the SQL Primary Key for that model. However, the field used as the Primary Key can be changed — to an email, for example — so when `pk` is referenced it would actually point to a field other than `id`.

It is safer to reference `pk` when in doubt.