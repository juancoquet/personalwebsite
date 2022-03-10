Note type: #litnote
Source: [[📖 Effective Python]] item 84

---
# Documenting functions
Every function and method should have a docstring that follows the same formula as module and class-level docstrings. The first line should be a single-sentence description of what the function does. The subsequent lines and paragraphs should describe any specific behaviours and the arguments that the function takes, as well as mentioning return values. Any exceptions that should be handled by the caller should also be explained.
```python
def find_anagrams(word, dictionary):
    """Find all anagrams for a word.

    This function only runs as fast as the test for
    membership in the 'dictionary' container.

    Args:
        word: String of the target word.
        dictionary: collections.abc.Container with all
            strings that are known to be actual words.

    Returns:
        List of anagrams that were found. Empty if
        none were found.
    """
```

A single sentence will suffice for simple functions that take no arguments and return a simple value—use discretion. If a function doesn't have a return value, it's best to not mention any kind of return instead of saying "returns None". Funciton docstrings should describe the circumstances in which the function's interface will raise exceptions. If a function accepts a variable number of arguments or keyword arguments, use `*args` and `**kwargs` to describe their purpose in the list of arguments. Mention any default values for arguments. If the function is a generator, the docstring should describe what the generator yields when it is iterated.

---
#### See also:
- [[Documenting modules]]
- [[Documenting classes]]
- [[Using `star-args` to accept a variable number of positional arguments]]
- [[Using `doublestar-kwargs` as a catch-all parameter]]
- [[Keyword-only arguments explained]]