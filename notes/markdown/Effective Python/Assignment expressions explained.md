Note type: #litnote
Source: [[📖 Effective Python]] item 10

---
# Assignment expressions explained
An assignment expression `:=` (also known as *the walrus operator*) allows you to assign variables in places where you normally wouldn't be able to (such as within an `if` statement) which can then be used in the proceeding code block.
```python
from random import randint

if result := randint(0, 2):	# result being assigned a value 0, 1 or 2
	print(10 / result)	# randint didn't evaluate to 0, we can divide
else:
	print("Can't divide because randint is {result}")
```

In the above example, the assignment expression first assigns a value to the `result` variable (a random integer between 0 and 2), and then evaluates it within the context of the `if` statement. If `randint` evaluated to 1 or 2 then the `if` statement evaluates to `True`. If `randint` evaluated to 0 then the `if` statement evaluates to `false` and the `else` block is called.

This can be clearer than assigning the variable before a code block:
```python
from random import randint

result = randint(0, 2)

if result:
	print(10/ result)
else:
	print("Cant divide becuase randint is {result}")
```

Proper use of the walrus operator can streamline code and improve readability as it keep variables embedded within the code blocks where they'll be used.