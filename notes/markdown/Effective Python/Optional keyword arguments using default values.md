Note type: #litnote
Source: [[📖 Effective Python]] item 23

---
# Optional keyword arguments using default values
By providing a default value for a parameter when defining a function, this becomes a default value when no argument is passed into the function for this parameter. This reduces noise and repetition, and is useful for when a function requires one value most of the time with some exceptions. This means that the argument needs to only be provided when exceptions are required, and the rest of the time it will use the default value.