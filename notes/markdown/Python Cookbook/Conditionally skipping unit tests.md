Note type: #litnote
Source: [[📖 Python Cookbook]] ch14.5 p573

---
# Conditionally skipping unit tests
The `unittest` module comes with decorators to conditionally skip tests.
```python
import unittest

class MyTest(unittest.TestCase):
	
	@unittest.skipIf({conidion}, {output message})
	def test_1(self);
		...
	
	@unittest.skipUnless({condition}, {output message})
	def test_2(self):
		...
	
	@unittest.expectedFailure		# Runs, but doesn't report extra info
	def test_3(self):
		self.assertEqual(2 + 2, 5)
		
```

The `skipIf` and `skipUnless` are good for running platform-specific tests, such as only running a test if the program is being run on Mac OS. This can be done by providing this condition to the `{condition}` placeholder above—`@skipUnless(platform.system() == 'Darwin', 'Mac-specific test')`.

---
### See also:
- [[Basic `unittest` example]]