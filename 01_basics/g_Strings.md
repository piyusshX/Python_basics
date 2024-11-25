### String
You can create a string by enclosing text within single, double or even in triple quotes:

```python
str1 = 'Grey'
str2 = "Natsu"
str3 = """Happy"""
print(str1)
print(str2)
print(str3)
Grey
Natsu
Happy
```

Similar to other languages we can access string's individual values by indexing -

```python
str1 = 'Grey'
print(str1[1])
r
```

### Operations in String

#### Slice in String
Slicing: You can extract a substring using slicing.

Syntax : str_name[`starting_Index` : `ending_Index + 1`]

In python string slicing ending index is not inclusive, that's why we have write (`ed_idx + 1`) in syntax.

```python
myStr = 'Hero Acadmia'
subStr = myStr[0:4]
print(subStr)
Hero
```

- Some more functionality in Slicing

```python
numList = "0123456789"

# What if we only give starting_Index
print(numList[3:])
3456789

# What if we only give ending_Index
print(numList[:6])
012345

# What if we use -ve index
numList[3: -4]
'345'
```

- Hopping - "hopping" in slicing refers to using a step value to skip elements when slicing a sequence like a string, list, or tuple.

Syntax - str[ `start` : `end` : `step` ]

```python
numList = '0123456789'

print(numList[0:7:2])
0246
print(numList[0:7:3])
036
numList[0:9:4]
048
```

- **Concatenation** : ***You can concatenate (join) two or more strings using the `+` operator***.

```python
greeting = "Hello, " + "World!"
print(greeting)
Hello, World
```


- **Repetition** : ***You can repeat strings using the `*` operator***.

```python
repeated = "Ha" * 3  # "HaHaHa"
print(repeated)
HaHaHa
```

#### Common String Methods

- **`len()`** : ***Returns the length of the given string.***

```python
len("hello")  # 5
```


- **`lower()`** : ***Converts the string to lowercase***.

```python
"HELLO".lower()  # "hello"
```


- **`upper()`** : ***Converts the string to uppercase.***

```python
"hello".upper()  # "HELLO"
```


- **`strip()`** : ***Removes leading and trailing whitespace.***

```python
"   Hello World  ".strip()  # "Hello World"
```


- **`replace()`** : ***Replaces a substring with another substring.***

```python
"Hello, World!".replace("World", "Blank")  # "Hello, Blank!"
```


- **`split()`** : ***Splits a string into a list of substrings based on a delimiter. If we dont pass a delimiter then it will split the string based on space.***

```python
mc = "Deku, Goku, Yuuji, Natsume"
mcList = mc.split(", ") 
print(mcList)
['Deku', 'Goku', 'Yuuji', 'Natsume']
```


- **`join()`** : ***Joins a list of strings into a single string with a separator.***

Syntax - `seperator.join(list)`

```python
myList = ['Deku', 'Goku', 'Yuuji', 'Natsume']
myHeroes = ", ".join(myList)
print(myHeroes)
Deku, Goku, Yuuji, Natsume
```


- **`find()`** : ***finds the substring in the given string and returns it's index and if not exist and returns `-1`.***

```python
myChai = "Masala Chai"
print(myChai.find('Chai'))
7
print(myChai.find('chai'))
-1
```


- **`count()`** : ***returns the count of a substring in the given string.***

```python
myChai = "Masala Chai Chai Chai"
print(myChai.count('Chai'))
3
print(myChai.find('chai'))
0
```


#### String Formatting

In Python, string formatting allows you to inject variables or expressions into strings, making them more dynamic and readable.

Python provides several ways to format strings -

1. **`str.format()` Method** : ***The `format()` method is an older but still widely used string formatting technique.***

- Syntax - "some string {}".format(var)

```python
name = "Piyush"
age = 19
greeting = "My name is {}, and I am {} years old."
print(greeting.format(name, age))
My name is Piyush, and I am 19 years old.

# Keyword Arguments : You can refer to variables by keyword names.
greeting = "My name is {name}, and I am {age} years old.".format(name="Alice", age=25)
My name is Alice, and I am 25 years old.

```


2. **`F-Strings`** : ***F-strings (formatted string literals) are the most modern and recommended way of formatting strings in Python.***

- It is similar to `format()` method but `F-strings` allows expressions and variables inside the curly braces.

- Syntax - `f`"some string `{var}`"

```python
show_name = "Natsume Yuujinchou"
season = 7
conversation = f"My Favirate show is {show_name}, and It only had {season} seasons."
print(conversation)
My Favirate show is Natsume Yuujinchou, and It only had 7 seasons.
```

### Double quotes inside a string

When we try to write double quotes inside a string to denote something like a quote or to highlight a word, then Python throws an error beacuse it is not able to understand it.

#### Backward Slash 

To solve above problem we can use backward slash `\` in our string to inform Python about it.

Syntax - "Some string `\"some text\"` more string"

```python
convo = "He said to me \"Bro! that anime was really good\""
print(convo)
He said to me "Bro! that anime was really good"
```

#### Raw String

A raw string in Python, is a string where escape sequences (like `\n` for newline or `\t` for tab or `\` used in path of windows) are not processed and are treated as literal characters. In Python, raw strings are defined by prefixing the string with an `r`.

- **Normal string** : `"Hello\nWorld"` will interpret `\n` as a newline, displaying as

```python 
Hello
World
```

- **Raw string** : `r"Hello\nWorld"` will display the `\n` as-is

```python 
Hello\nWorld
```

Raw strings are very useful in case of handling windows paths since they includes `\` in it.

```python
path = "c:\user\pwd" # give error
File "<python-input-38>", line 1
    path = "c:\user\pwd"

# We can solve the above issue by adding double slash but using raw string is more prefered
path = "c:\\user\\pwd"
print(path)
c:\user\pwd

path = r"c:\user\pwd"
print(path) # c:\user\pwd
```