Author: [[👤 Brett Slatkin]]
Type: #book
Genres: #comp-sci

---
# Effective Python
## 90 Specific Ways to Write Better Python

### 1 Pythonic Thinking
#### Item 2: Follow the PEP 8 Style Guide
- [[Indent line continuations]]
- [[Pythonic naming conventions]]
- [[Use inline negation over negation of positive expressions]]
- [[Surround multi-line expressions in parentheses]]
- [[Import using absolute module names over relative module names]]
- [[Import statement sections and order]]

#### Item 3: Know the Differences Between `bytes` and `str`
- [[`bytes` instances are incompatible with `str` instances]]
- [[Writing and reading binary data to and from files]]

#### Item 4: Prefer Interpolated F-Strings over C-style Format Strings
- [[What is string formatting]]
- [[Advanced .format specifier uses]]
- [[Interpolated f-strings allow referencing of any variable in the current scope]]
- [[F-strings allow a full expression to be placed within specifier braces]]

#### Item 5: Write Helper Functions Instead of Complex Expressions
- [[Break down complex expressions into helper functions to improve readability]]
- [[Follow the DRY principle – Don't Repeat Yourself]]

#### Item 6: Prefer Multiple Assignment Unpacking Over Indexing
- [[Multiple assignment unpacking explained]]
- [[Use multiple assignment unpacking to swap values in place]]
- [[Use multiple assignment unpacking to unpack iterables in loops]]

#### Item 7: Prefer `enumerate` Over `range`
- [[How `enumerate` works]]
- [[`enumerate` yielded pairs can be unpacked in a `for` statement]]

#### Item 8 Use `zip` to Process Iterators in Parallel
- [[How `zip` works]]
- [[Use `zip_longest` as an alternative when necessary]]
- [[Using `zip` instead of indexing to handle multiple iterables]]

#### Item 10: Prevent Repetition with Assignment Expressions
- [[Assignment expressions explained]]
- [[Assignment expressions can be combined with comparison and logical operators as part of logical expressions]]

### 2 Lists and Dictionaries
#### Item 11: Know How to Slice Sequences
- [[List slicing syntax]]
- [[Slicing from and to list boundaries]]
- [[Slicing a copy of a list]]
- [[Negative indexing slices]]
- [[Slices do not modify the original list]]
- [[Using slices in assignments]]

#### Item 12: Avoid Striding and Slicing in a Single Expression
- [[Striding syntax explained]]
- [[Negative stride values]]
- [[Simplifying striding and slicing for readability]]

#### Item 13: Prefer Catch-All Unpacking Over Slicing
- [[Catch-all unpacking syntax explained]]
- [[Catch-all unpacking is more readable than indexing and slicing]]

#### Item 14: Sort by Complex Criteria Using the `key` Parameter
- [[Lists can be sorted by a specific attribute]]
- [[Tuples are sorted left to right]]
- [[Sorting by multiple criteria]]

#### Item 15: Be Cautious When Relying on `dict` Insertion Ordering
- [[Dictionaries were not ordered before Python 3.6]]

#### Item 16: Prefer `get` Over `in` and `KeyError` to Handle Missing Dictionary Keys
- [[Using `get` to check for existence of a `key` in a `dict` type]]

#### Item 17: Prefer `defaultdict` Over `setdefault` to Handle Missing Items in Internal State
- [[`defaultdict` automatically sets a default value to missing keys]]

#### Item 18: Know How to Construct Key-Dependent Default Values with `__missing__`
- [[ `__missing__` method explained]]

### 3 Functions
#### Item 19: Never Unpack More Than Three Variables When Functions Return Multiple Values
- [[Individually unpacking more than 3 return values hurts readability]]

#### Item 20: Prefer Raising Exceptions to Returning `None`
- [[Returning `None` can be error prone]]

#### Item 21: Know How Closures Interact with Variable Scope
- [[Closure functions are able to access but not overwrite variables in higher scopes]]

#### Item 22: Reduce Visual Noise with Variable Positional Arguments
- [[Using `star-args` to accept a variable number of positional arguments]]

#### Item 23: Provide Optional Behaviour with Keyword Arguments
- [[Dictionaries can be used for providing keyword arguments in function calls]]
- [[Using `doublestar-kwargs` as a catch-all parameter]]
- [[Optional keyword arguments using default values]]

#### Item 24: Use `None` and Docstrings to Specify Dynamic Default Arguments
- [[Default arguments are evaluated on module load]]

#### Item 25: Keyword-Only and Positional-Only Arguments
- [[Keyword-only arguments explained]]
- [[Positional-only arguments explained]]

#### Item 26: Define Function Decorators with `functools.wraps`
- [[Using `functools.wraps` for decorators]]

### 4 Comprehensions and Generators
#### Item 27: Use Comprehensions Instead of `map` and `filter`
- [[Comprehensions can affect and filter items in a list more clearly than `map` and `filter`]]

#### Item 28: Avoid More Than Two Control Sub-expressions in Comprehensions
- [[Multiple looping in comprehensions]]
- [[Comprehensions support multiple `if` statements]]

#### Item 29: Avoid Repeated Work in Comprehensions by Using Assignment Expressions
- [[Using assignment expressions in conditional statements]]

#### Item 30: Consider Generators Instead of Returning Lists
- [[Using generators]]

#### Item 31: Be Defensive When Iterating Over Arguments
- [[Iterables are not the same as iterators]]
- [[Be careful using functions and methods that iterate over input arguments]]

#### Item 32: Consider Generator Expressions for Large List Comprehensions
- [[Generator expressions explained]]

#### Item 33: Compose Multiple Generators with `yield from`
- [[Use `yield from` when looping through a generator to create another generator]]

#### Item 36: Consider `itertools` for Working with Iterators and Generators
- [[`itertools.chain`]]
- [[`itertools.repeat`]]
- [[`itertools.cycle`]]
- [[`itertools.tee`]]
- [[`itertools.zip_longest`]]
- [[`itertools.islice`]]
- [[`itertools.takewhile`]]
- [[`itertools.dropwhile`]]
- [[`itertools.filterfalse`]]
- [[`itertools.accumulate`]]
- [[`itertools.product`]]
- [[`itertools.permutations`]]
- [[`itertools.combinations`]]
- [[`itertools.combinations_with_replacement`]]


### 5 Classes and Interfaces
#### Item 37: Compose Classes Instead of Nesting Many Levels of Built-in Types
- [[When nesting many built-in types becomes complicated, you should refactor into classes]]

#### Item 38: Accept Functions Instead of Classes for Simple Interfaces
- [[Using `__call__` to define behaviour when an object is called]]

#### Item 40: Initialise Parent Classes with `super`
- [[Use `super()` to inherit from a parent class]]

#### Item 42: Prefer Public Attributes Over Private Ones
- [[Public attributes vs private attributes]]
- [[Prefer protected attributes over private attributes]]

#### Item 43: Inherit from `collections.abc` for Custom Container Types
- [[Inheriting from `collections.abc`]]

### 6 Metaclasses and Attributes
#### Item 44: Use Plain Attributes Instead of Setter and Getter Methods
- [[Access attributes through dot notation, not methods]]

### 8 Robustness and Performance
#### Item 65: Take Advantage of Each Block in `try/except/else/finally`
- [[`finally` Blocks]]
- [[`else` blocks]]

#### Item 66: Consider `contextlib` and `with` Statements for Reusable `try/finally` Behaviour
- [[Using `contextmanager` to use custom functions in `with` statements]]

#### Item 67: Use `datetime` Instead of `time` for Local Clocks
- [[Use `datetime` to convert to different time zones]]

#### Item 68: Make `pickle` Reliable with `copyreg`
- [[What is `pickle`]]
- [[Using `pickle`]]
- [[Using `copyreg` to load outdated class instances reliably]]

#### Item 69: Use `decimal` When Precision is Paramount
- [[Using `decimal`]]

#### Item 70: Profile Before Optimising
-  [[Using `Profile`]]

#### Item 71: Prefer `deque` for Producer-Consumer Queues
- [[Using `deque` for FIFO structures]]

#### Item 72: Consider Searching Sorted Sequences with `bisect`
- [[Using `bisect`]]

#### Item 73: Know How to Use `heapq` for Priority Queues
- [[Using `heapq`]]

#### Item 83: Use Virtual Environments for Isolated and Reproducible Dependencies
- [[Do not install packages globally]]
- [[Using `venv` to create a virtual environment]]
- [[Recreating dependencies with `freeze`]]

#### Item 84: Write Docstrings for Every Function, Class, and Module
- [[Documenting modules]]
- [[Documenting classes]]
- [[Documenting functions]]

#### Item 85: Use Packages to Organise Modules and Provide Stable APIs
- [[What are python packages]]
- [[Importing python packages]]
- [[Using `__all__` to provide stable APIs]]
- [[Making a public API]]

#### Item 87: Define a Root `Exception` to Insulate Callers from APIs
- [[Inheriting from `Exception`]]
- [[Using an exception base-class]]

#### Item 88: Know How to Break Circular Dependencies
- [[Fixing circular module interdependence]]
- [[Dynamic imports]]

#### Item 89: Consider `warnings` to Refactor and Migrate Usage
- [[The `warnings` module explained]]

#### Item 90: Consider Static Analysis via `typing` to Obviate Bugs
- [[How to use `typing`]]