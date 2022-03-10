Note type: #litnote
Source: [[📖 Effective Python]] item 19

---
# Individually unpacking more than 3 return values hurts readability
While unpacking indefinite return values works perfectly fine, this can become visually noisy and difficult to read. Instead, when more than 3 return values need to be unpacked, consider a starred catch-all expression to avoid visual noise and avoid having to use awkward line-wrapping when calling and unpacking functions that return many values.

Where many values need to be returned, consider instead returning a small class instance to avoid the error prone nature of unpacking many return values, where they can become easily mixed up.

---
#### See also:
- [[Catch-all unpacking syntax explained]]