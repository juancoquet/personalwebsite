Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 1.13.2
Date: 2021-10-27

---
# Parent classes can call methods that don't yet exist
A powerful feature of object-oriented programming is calling code in a parent class that has not yet been defined, with the idea to define the missing behaviour in child classes.

As a toy example, imagine we are defining a parent class of `Shape`, which will later be sub-classed by different kinds of geometric shapes. We can give our `Shape` superclass a `get_area()` method, even though the subclasses that represent different kinds of shapes will have different formulas to calculate the area.

```Python

class Shape:

	def __init__(self):
		...
	
	def get_area(self):
		self.area = self.calculate_area()
		return self.area

```

With this architecture, we can now define a custom `calculate_area()` method in each subclass, which will in turn be called by `get_area()`. This seems like a trivial example as we could just skip the `get_area()` step and call `calculate_area()` directly for all different shape types, but with more complex data structures where functionality is partially shared this is a very powerful way to organise code.

For example, imagine that (for whatever reason) we frequently needed to get the object's area value doubled. We could define the following method as part of the `Shape` superclass to avoid continually using `*2` in the body of our code, and to avoid having to write this behaviour for every single subclass:

```Python

class Shape:

	...
	
	def get_area_doubled(self):
		self.area = self.calculate_area()
		return self.area * 2

```

`calculate_area()` will be uniqely defined by inheritants of `Shape`, but they will all be able to call `get_area_doubled()` in the same way.