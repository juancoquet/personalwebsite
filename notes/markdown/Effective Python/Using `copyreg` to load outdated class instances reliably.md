Note type: #litnote
Source: [[📖 Effective Python]] item 68

---
# Using `copyreg` to load outdated class instances reliably
The `pickle` module is intended to make object serialisation and desirialisation easy, but it is not intended to be completely robust beyond trivial use cases. For example, loading an old object instance after the overarching class' attributes have changed will result in an object which doesn't account for the changed class attributes—it will be a carbon copy of the original object even if the class it belongs to has changed.

To fix this problem, `copyreg` can be used to define behaviour for unpickling an object back into a program. To do this, we must define a constructor (`__init__`) function with keyword arguments and default values, and a helper function that returns a function to use for unpickling along with the parameters to be passed into the new object instance:
```python
import copyreg
import pickle

class GameState():
	def __init__(self, level=1, lives=5):		# keyword arguments and default values
		self.level = level
		self.lives lives

def pickle_game_state(game_state_object):
	kwargs = game_state_object.__dict__		# pulling out parameters into a variable
	return unpickle_game_state, (kwargs,)	# returning an unpickling func (defined below) and the kwargs to be used
	
def unpickle_game_state(kwargs):
	return GameState(**kwargs)			# returns a GameState instance with the kwargs as arguments

copyreg.pickle(GameState, pickle_game_state)		# registering the function to be used for serialising and deserialising
```

The object can now be pickled and unpickled and be kept up-to date with changes to its overarching class, as each time the object is unpickled back into the program a `GameState` instance is created using the `**kwargs` arguments, meaning that any missing arguments will be set to the default value upon instantiation.

---
#### See also:
- [[Using `doublestar-kwargs` as a catch-all parameter]]
- [[Using `pickle`]]