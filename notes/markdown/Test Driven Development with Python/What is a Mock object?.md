Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch19 p328

---
# What is a Mock object?
A Mock object is an object that responds to any request for an attribute or method call — it will never raise `AttributeError`. It can also be configured to return specific values for calls of its ubiquitous methods and attributes, and we can use the special `.called` and `.call_args` attributes to check if a method of the Mock object was called, and what arguments it was called with. It can be imported directly from `unittest.mock`, but it is also used implicitly in the implementation of the `@patch` decorator (also from `unittest.mock`). Consider the following shell session to illustrate the concepts:
```python shell
>>> from unittest.mock imprt Mock
>>> m = Mock()
>>> m.any_attribute		# random attribute call
<Mock name='mock.any_attribute' id='124750920894'>
>>> type(m.any_attribute)
<class 'unittest.mock.Mock'>
>>> m.any_method()		# random method call
<Mock name='mock.any_method()' id='1249782170535'
>>> m.foo()
<Mock name='mock.foo()' id='12452710987'
>>> m.foo.called	# check if foo() method has been called
True
>>> m.bar.return_value = 1		# specify return for .bar() method
>>> m.bar(42, arg='thing')		# call .bar() with args
1								# returns specified value, 1
>>> m.bar.call_args				# check args .bar() was called with
call(42, arg='thing')
```

---
### See also:
- [[Using `@patch` for mocking]]