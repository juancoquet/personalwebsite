Note type: #litnote
Source: [[📖 Effective Python]] item 68

---
# Using `pickle`
Below is an example of how one might use `pickle` to save the state of a game. We define a game state class which keeps track of the information, then we `dump` this object into a file using `pickle` to store is as a `bytes` stream so that it can then be recalled in another session, thus saving the state of the game.
```python
import pickle

class GameState:
	def __init__(self):
		self.level = 1
		self.lives = 5
		
# playing:
state = GameState()
state.level += 1		# player leveled up
state.lives -= 1		# player lost a life

# saving state
with open('save_game.bin', wb) as f:		# opening save file in write bytes mode
	pickle.dump(state, f)					# dumping the `state` object into 'save_game.bin' file using pickle
```

I can later recall this object into the program by using `pickle.load` in a different session
```python
with open('save_game.bin', rb) as f:		# opening save file in read bytes mode
	loaded_state = pickle.load(f)			# deserialising object into the program
```

The `load_state` variable now holds the original `GameState` object and can be used in the program.

---
#### See also:
- [[Using `pickle`]]