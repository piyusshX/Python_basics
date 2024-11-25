### List 

In Python, a `list` is a `mutable`, ordered collection of items that can hold elements of any data type, including other lists. You can create and manipulate lists with various methods and operators. 

List is very much similar to `array` in Javascript.

```python
# Empty list
my_list = []

# List with elements
my_list = [1, 2, 3, "apple", 4.5, True]

print(my_list)
[1, 2, 3, "apple", 4.5, True]

print(my_list[2])
3

print(my_list[3])
apple
```

#### Modifying a List

In Python we modify list in a same way how we modify an array in Javascript.

```python
my_list = [1, 2, 3, "apple", 4.5, True]

# Changing an element
my_list[0] = "banana"  
print(my_list)
["banana", 2, 3, "apple", 4.5, True]

# Adding elements
my_list.append("new_item")  # Adds to the end
print(my_list)
["banana", 2, 3, "apple", 4.5, True, "new_item"]

my_list.insert(1, "inserted_item")  # Adds at index 1
print(my_list)
["banana","inserted_item", 2, 3, "apple", 4.5, True, "new_item"]

# Removing elements
my_list.remove("apple")  # Removes "apple" from the list
print(my_list)
["banana","inserted_item", 2, 3, 4.5, True, "new_item"]

popped_item = my_list.pop()  # Removes and returns the last item
print(my_list)
["banana","inserted_item", 2, 3, 4.5, True]
```

#### Slice in List

Slicing: You can extract a sublist using slicing.

Syntax : list_name[`starting_Index` : `ending_Index + 1`]

In python list slicing ending index is not inclusive, that's why we have write (`ed_idx + 1`) in syntax.

```python
my_list = [0, 1, 2, 3, 4, 5]
sub_list = my_list[0:4]
print(sub_list)
[0, 1, 2, 3]
```

- Some more functionality in Slicing

```python
my_list = [0, 1, 2, 3, 4, 5]

# What if we only give starting_Index
print(my_list[3:])
[3, 4, 5]

# What if we only give ending_Index
print(my_list[:4])
[0, 1, 2, 3]

# What if we use -ve index
my_list[2: -2]
[2, 3]
```

- Hopping - "hopping" in slicing refers to using a step value to skip elements when slicing a sequence like a string, list, or tuple.

Syntax - str[ `start` : `end` : `step` ]

```python
numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numList[0:7:2])
[0, 2, 4, 6]
print(numList[0:7:3])
[0, 3, 6]
numList[0:9:4]
[0, 4, 8]
```

##### Note - In some cases people try to modify values in list using slicing, so if you are also trying to modify list using slicing give the modified value in list too. Otherwise you'll see some unexpected results.

```python
hero = ["deku", "shoto", "uravity", "goku"]

hero[2:3] = "bakugo" # hero[2:3] = "uravity"
print(hero)
['deku', 'shoto', 'b', 'a', 'k', 'u', 'g', 'o', 'goku']

# So what happend above python treated "bakugo" as list and added 
# each individual charater one-by-one in place of 2nd index.

# So to fix this we have to explicitly give a list if we're performing modification using slicing
hero = ["deku", "shoto", "uravity", "goku"]
hero[2:3] = ["bakugo"]
print(hero)
['deku', 'shoto', 'bakugo', 'goku']

my_tea = ["lemon", "green", "chai", "Oolong"]
my_tea[1:3] = ["masala"] # my_tea[1:3] = ["green", "chai"]
print(my_tea)
['lemon', 'masala', 'Oolong']
```

```python
my_tea = ["lemon", "green", "chai", "Oolong"]
print(my_tea[1:1])
[]

my_tea[1:1] = ["ginger", "arjun tea"]
print(my_tea)
["lemon","ginger", "arjun tea", "green", "chai", "Oolong"]

my_tea[1:2] = [] # my_tea[1:2] = ["ginger", "arjun tea"]
print(my_tea)
["lemon", "green", "chai", "Oolong"]
```

#### `copy()`

In Python, the `copy()` method is used to create a `shallow copy` of a list. A `shallow copy` means that it creates a new list with references to the same elements as the original list, but it does not duplicate any nested lists or other complex objects inside it. This is useful if you want to duplicate a list but don't want modifications to one list to affect the other.
```python
my_list = [0, 1, 2, 3] # stored in memoryAdd = x500
copy_list = my_list # now copy_list is also pointing to x500
# To avoid this we use copy method
copy_list = my_list.copy() # stored in memoryAdd = x600
```

#### List Comprehension
You can create a list based on an existing list or a range of values:

```python
print(range(10))
range(0, 10) # gives the range from 0 to 9
# 10 is exclusive 

squared_num = [x**2 for x in range(10)]
print(squared_num)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cube_num = [x**3 for x in range(10)]
print(cube_num)
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

squares = [x ** 2 for x in range(1, 6)]  
print(squares)
[1, 4, 9, 16, 25]
```
