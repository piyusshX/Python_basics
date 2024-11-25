### Dictionary in Python

Same as Objects in Javascript
- Syntax - {"`key`" : "`value`"}
- Syntax - dict(`key`="`value`")

```Python
# Using curly braces
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Using dict() function
my_dict = dict(name="Alice", age=25, city="New York")
```

#### Accessing Values

- Access values by their keys.

```Python
print(my_dict["name"])  # Output: Alice
```

- Access value by `get()` method

```Python
print(my_dict.get("name"))  # Output: Alice
```

#### Adding or Updating Elements

You can add a new key-value pair or update an existing key's value.

```Python
my_dict["age"] = 26  # Update existing key
my_dict["country"] = "USA"  # Add new key
```

#### Looping in Dictionary

- Method 1 

```Python
character = {"mha" : "deku", "nbf" : "natsume", "ft" : "natsu"}

for key in character:
    print(key) 

# mha
# nbf
# ft

# As we can see we get keys not value

for key in character:
    print(character[key])

# deku
# natsume
# natsu

for key in character:
    print(key,":", character[key])

# mha : deku
# nbf : natsume
# ft : natsu
```

- Method 2 - by using `items()` method

```Python
for key, value in character.items():
    print(key,":", value)

# mha : deku
# nbf : natsume
# ft : natsu
```

#### Removing Elements

1. `pop()` method - We need to give key to remove the element. this method returns the value of the given key.

- Syntax - `my_dict.pop("key")`

```Python
character = {"mha" : "deku", "nbf" : "natsume", "ft" : "natsu"}

character.pop("mha")
# returns 'deku'

print(character)
{'nbf': 'natsume', 'ft': 'natsu'}
```

2. `popitem()` method - pops the last added value to the dictionary and it returns the poped key-value pair tuple.

- Syntax - `my_dict.popitem()`

```Python
character = {"mha" : "deku", "nbf" : "natsume", "ft" : "natsu"}

character["dbz"] = "goku"
print(character)
{"mha" : "deku", "nbf" : "natsume", "ft" : "natsu", "dbz" : "goku"}

character.popitem()
# returns ('dbz', 'goku')

print(character)
{"mha" : "deku", 'nbf': 'natsume', 'ft': 'natsu'}
```

3. `del` - deletes the refrence of the give key from the memory

```Python
del my_dict["key"] 
# returns {"key" : "value"}
```

#### if condictional

- Syntax - if `key` in `dict`:

```Python
character = {"mha" : "deku", "nbf" : "natsume", "ft" : "natsu"}
if "nbf" in character:
    print("Natsume's Book of Friends is present!")
```

#### Dictionary Comprehension

```python
square = {x : x**2 for x in range(6)}
print(square)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#### `clear()` method -

As the name suggest it clears out the dictionary.

- Syntax - `dict.clear()`
```python
square = {x : x**2 for x in range(6)}
print(square)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

square.clear()
print(square)
{}
```

#### `fromkeys()` method 

```python
key = ["mha", "ft", "nbf", "jjk"]
value = ["deku", "natsu", "natsume", "yuuji"]
default_val = "good anime"

new_dict = dict.fromkeys(key, default_val)
print(new_dict)
{'mha': 'good anime', 'ft': 'good anime', 'nbf': 'good anime', 'jjk': 'good anime'}

character_dict = dict.fromkeys(key, value)
print(character_dict)
{'mha': ['deku', 'natsu', 'natsume', 'yuuji'],
 'ft': ['deku', 'natsu', 'natsume', 'yuuji'], 
 'nbf': ['deku', 'natsu', 'natsume', 'yuuji'], 
 'jjk': ['deku', 'natsu', 'natsume', 'yuuji']}
```

We can see the behavior of `fromkeys()` method in the above code.