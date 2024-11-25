### Tuples

A tuple in Python is a built-in data structure that allows you to store a collection of items. 

It is basically same as list or we can even say that tuple is nothing but immutable list.

A tuple is a collection type similar to a list but is immutable and generally used for fixed data.

- **Immutable**: Once a tuple is created, its contents cannot be changed (i.e., you cannot add, remove, or modify elements).

- **Ordered**: Tuples maintain the order of the elements as they are defined.

- **Heterogeneous**: Tuples can contain items of different data types, such as integers, strings, or even other tuples.


```python
my_tup = ("deku", "natsu", "natsume")
print(my_tup)
('deku', 'natsu', 'natsume')

print(my_tup[1])
natsu

my_tup[1] = "happy" # Throw error

Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    my_tup[1] = "happy"
    ~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

### Common Operations

#### Accessing Tuple Elements

You can access elements in a tuple using indexing, which starts at 0:

```python
print(my_tup[1])  # Output: natsu
```


#### Concatenation

You can combine tuples using the `+` operator:

```python
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2  # Output: (1, 2, 3, 4)
```


#### Repetition

You can repeat tuples using the `*` operator:

```python
repeated = (1, 2) * 3  # Output: (1, 2, 1, 2, 1, 2)
```

#### `in` keyword

You can check if an item exists in a tuple using the `in` keyword:

```python
print("natsu" in my_tup)  # Output: True
```

#### `count()` keyword

You can check the count of the given value by using `count()` keyword:

```python
new_tup = ("natsu", "natsu", "natsume", "yuuji")
new_tup.count("natsu") # 2
```

#### Unwraping of tuple 

```python
my_tup = ("natsume", "natsu", "yuuji", "reiko")
(nbf, ft, jjk, ny) = my_tup # nbf, ft, jjk -> are variables

# number of variables must be equal to no of elements in tuple

print(nbf)
'natsume'

print(ny)
'reiko'
```