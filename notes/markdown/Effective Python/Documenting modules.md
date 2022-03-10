Note type: #litnote
Source: [[📖 Effective Python]] item 84

---
# Documenting modules
Each module should begin with a docstring to introduce the module and its contents. This is done by using three double quotes """. The first line should describe the module's overall purpose, with subsequent lines and paragraphs containing any details that the user should know about its operation. Any important classes and functions should be highlighted here.
```python
"""Library for finding linguistic patterns in words.

Testing how words relate to each other can be tricky sometimes!
This module provides easy ways to determine when words you've
found have special properties.

Available functions:
- palindrome: Determine if a word is a palindrome.
- check_anagram: Determine if two words are anagrams.
"""
```