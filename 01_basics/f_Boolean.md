### Boolean

In Python boolean datatype is treated as Number internally (`True == 1 and False == 0`). But you cannot say that `True` and `1` are actually same as well as `False` and `0` are same.

```python
type(True)
<class 'bool'>

True == 1
True

False == 0
True

# As we can see that python is treating True and 1 as equal and False and 0 as equal.
# But are they actually same?
True is 1
<python-input-98>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
# Meaning both True and 1 are treated as different object and they are not same.
# But there values are same.

# we can also do this 
True + 5
6
```
