### Set in Python
Sets in python is same as sets in maths. We can declare set in the Python same as maths. 

We can also performs the Operations like Union `|`, Intersection `&` and Difference `-` etc.

```python
# Declaration
setOne = {1, 2, 3, 4}

# Union(|)
setOne | {5, 6, 7}
{1, 2, 3, 4, 5, 6, 7}

# Intersection(&)
setOne & {2, 4}
{2, 4}

# Difference(-)
setOne - {2, 4}
{1, 3}
```

Note -> In Python empty set is denoted by `set()` instead of `{}`. Beacuse `{}` is consider dictionary type.
```python
setOne = {1, 2, 3, 4}
setOne - {1, 2, 3, 4}
set()

type(setOne - {1, 2, 3, 4})
<class 'set'>

type({})
<class 'dict'>
```