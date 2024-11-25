#### Concept of Shallow and Deep Copy

When we use `copy()` method to create a copy of list then Python create a shallow copy of it, In Shallow copy the outer list is duplicated, but each nested list or object inside it is not duplicated.

Both the original and the copied list point to the same nested lists in memory. Therefore, changes to a nested list in either the original or copied list will affect both lists, as they share the same nested objects.

```python
original_list = [1, 2, [3, 4]]
shallow_copy = original_list.copy()
```

- `shallow_copy` creates a new, independent list for the outer structure.
- However, the nested list `[3, 4]` is not duplicated. Instead, `shallow_copy` references the same nested list `[3, 4]` as `original_list`.

```python
shallow_copy[2][0] = 100
print(original_list)  # [1, 2, [100, 4]]
print(shallow_copy)   # [1, 2, [100, 4]]
```

Both `original_list` and `shallow_copy` reflect the change because they share the same nested list `[3, 4]` (now `[100, 4]`). This happens because a shallow copy does not create separate copies of nested lists.

### Deep Copy

If we want to create a copy where even nested objects are duplicated, we need to use the deepcopy() function from the copy module:

```python

import copy

deep_copy = copy.deepcopy(original_list)
deep_copy[3][0] = 700

print(original_list)  # [1, 2, 3, [400, 5]]
print(deep_copy)      # [100, 2, 3, [700, 5]]

```

With `deepcopy()`, changing nested objects in the copied list does not affect the original list.