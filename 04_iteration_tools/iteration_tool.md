#### Iterator

In Python, an iterator is an object that allows you to traverse through a sequence of elements one at a time. It is a fundamental concept in Python, often used in loops and data processing.

- An object that can return an iterator using the `iter()` function is called Iterable.
- Examples: Lists, tuples, dictionaries, strings, and other collections are iterables.
- You can create an iterator by calling `iter()` on an iterable, like a list, dictionary, range, string etc.

```python
# Example list
my_list = [1, 2, 3]

# Create an iterator from the list
my_iterator = iter(my_list)

print(my_iterator)
# <list_iterator object at 0x000001A5D5906A40>

```

As we can see in the above code that my_iterator is an list_iterator and is pointing object at some memory location.

#### `__next__()` / `next()` method - 

The `__next__()` method in Python is used to fetch the next item from an iterator. When you use a loop or manually call `__next__()`, it will retrieve the next item in the sequence until the iterator is exhausted.

- The `__next__()` method is used to get the next value from an iterator.
- `__next__()` will raise a `StopIteration` exception when there are no more items to return.

```python
# Manually fetch items using __next__()
print(my_iterator.__next__())  # Output: 1
print(my_iterator.__next__())  # Output: 2
print(my_iterator.__next__())  # Output: 3
print(my_iterator.__next__())  # Output: StopIteration

Traceback (most recent call last):
  File "<python-input-27>", line 1, in <module>
    print(my_iterator.__next__())
          ~~~~~~~~~~~~~~~~~~~~^^
StopIteration
```

- Instead of using `__next__()` we can simply use `next()`.

**`NOTE`** - As we know that iterator are iterable objects that points at some memory location. But remember that when we traverse the iterator by using `__next__()` or any other method the value of iterator or address stored in iterator does not change.

```python
my_list = [1, 2, 3]
my_iterator = iter(my_list)

print(my_iterator)
# <list_iterator object at 0x000001A5D5906A40>
print(my_iterator.__next__())  # Output: 1
print(my_iterator.__next__())  # Output: 2
print(my_iterator)  
# Output: <list_iterator object at 0x000001A5D5906A40>
```

#### Opening a File in python

In Python, opening a file is really simple and can be done by using the `open()` method.

File is an `iterator`. Since it by default has its own `iter()` function.

```python
f = open("./04_iteration_tools/script.py")
iter(f) is f # True
```

- Syntax - `open("file_path", "mode")`
- `mode` : Specifies how the file should be opened:

  - `r` - Read (default mode).
  - `w` - Write (creates a new file if it doesn’t exist or truncates the file if it exists).
  - `a` - Append (writes at the end of the file if it exists, or creates a new one).
  - `r+`, `w+`, `a+` - Read and write combined.

```python
f = open("./04_iteration_tools/script.py")
print(f.readline()) # prints first line of the file
# Output : 'import time\n'
print(f.read()) # prints all lines of the file
# Output : 'print("All Might - I AM HERE!")\nhero = "Deku"\nprint(hero)\n'
```

- `open()` method has alot of other parameters that can be passed like `endcoding`, `buffering`, etc.
- when there is not content left `.readline()` method returns an empty string.

Since File is an Iterator we can use next() method to fetch the next line from it.

```python
f = open("./04_iteration_tools/script.py")
next(f)# prints first line of the file
# Output : 'import time\n'
next(f) # 'print("All Might - I AM HERE!")\n'
next(f) # 'hero = "Deku"\n'
next(f) # 'print(hero)'
next(f) # Error - StopIteration
```

We can also use `for` loop to read the file line by line.

```python
for line in open('./04_iteration_tools/script.py'):
    print(line, end='')

# import time
# print("All Might - I AM HERE!")
# hero = "Deku"
# print(hero)
```

Similarly we can use `while` loop to read the file line by line.

```python
f = open('04_iteration_tools/script.py')
while True:
    line = f.readline()
    if not line: break
    print(line, end='')
```
