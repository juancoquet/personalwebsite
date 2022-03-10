Note type: #litnote
Source: [[📖 Effective Python]] item 20

---
# Returning `None` can be error prone
If a function can return a value of `None`, this can lead to errors when the function return is evaluated as part of a logical expression. If the caller knows that `None` is a possible output of the function, this may be used to test for `false`-equivalent values in an `if` statement, which would include not only `None` but also return values of 0, `False`, empty strings/lists/tuples etc.

This can lead to false-negatives occurring, where an `if` statement that the caller used intending to check for a return value of `None` does not discriminate between `None` and `[]`, for example.

Instead of returning `None`, raise an exception and include documentation to explain specifically what will trigger the exception to be raised. This will allow the caller to handle the exception outside of the function in whatever way is needed, thus reducing possible errors in the code.