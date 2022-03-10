Note type: #litnote
Source: [[📖 Effective Python]] item 84

---
# Documenting classes
Every class should have a class-level docstring which follows the same format as the module-level docstring. The first line is a single sentence stating the purpose of the class, with subsequent lines and paragraphs explain important details about the class' operation. Any important public attributes and methods should be highlighted here. There should also be guidance on how sub-classes should interact with protected attributes and the superclass' methods.
```python
class Player:
    """Represents a player of the game.

    Subclasses may override the 'tick' method to provide
    custom animations for the player's movement depending
    on their power level, etc.

    Public attributes:
    - power: Unused power-ups (float between 0 and 1).
    - coins: Coins found during the level (integer).
    """
```