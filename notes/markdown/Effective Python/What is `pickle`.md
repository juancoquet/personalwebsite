Note type: #litnote
Source: [[📖 Effective Python]] item 68

---
# What is `pickle`
`pickle` is a module that lets you turn any python object into a `bytes` stream, saved in a file—this is called serialising. This is a kind of export for a python object, as the `bytes` stream is essentially a set of instructions that can be run to reconstruct the original object. You can `pickle` the object to a `bytes` stream and then deserialise the bytes back into a python object in another program.