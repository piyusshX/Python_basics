# Functions / Defination -

Syntax - `def fun_name(parameters):`

```python
def my_def(para="Hello"): # default parameter
    return para

print(my_def("Hello World!"))
```

### Return multiple arguments
 
In Python, we can return more than one value

```python
def circle_stats(radius):
    area =  * (radius ** 2)
    circumference = 2 * 3.14 * radius
    return area, circumference

a, c = circle_stats(3)
print("Area :", a, "\nCircumference :", c)
```

### Lambda function


A lambda function in Python is an anonymous (nameless) function defined with the `lambda` keyword. Lambda functions are used for small, one-time tasks, especially when a function is only needed briefly or for a specific line of code. They are typically written in a single line and can only contain a single expression.

- Syntax - `lambda arguments: expression`
- `arguments` - The input(s) to the function (can have multiple arguments).
- `expression` - The computation or operation the function performs, returning the result.
- Lambda functions can take any number of arguments, but only one expression.

```python
cube = lambda x: x ** 3
print(cube(3))
```

### *args

In Python, `*args` is a way to allow a function to accept a variable number of positional arguments.

- It is used when we dont know number of arguments user going to give.
- When you define a function with `*args`, it collects all the positional arguments passed to the function and packs them into a `tuple`.
- This is useful when you don’t know in advance how many arguments will be passed to the function.

```python
def sum_all(*args):
    print(args) # (1, 2, 3)
    s = 0
    for i in args:
        s += s + i
    return s
    # return sum(args) # we can do this instead of above
print(sum_all(1, 2, 3))
```

- `*args` is just a convention; you could use any name, but `args` is standard.
- The function can handle any number of arguments due to `*args`.

### **kwargs

In Python, `**kwargs` allows a function to accept a variable number of keyword arguments, packing them into a `dictionary`. 

This is useful when you don’t know in advance what specific keyword arguments will be passed.

- It stores the arguments as key-value pairs in a dictionary.
-

```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(Hero="Deku", Power="One for All", Inspiration="All Might")
# Hero : Deku
# Power : One for All
# Inspiration : All Might
```

### `yield`

Similar to `return` keyword `yield` keyword also returns the value/iterator but ye memory me uss function ko rakta hai along with its state meaning kitna kaam ye function kar chuka hai. Iss liye yield keyword generator functions me zadatar use hota hai.

#### How yield Works - 

- When `yield` is used in a function, the function becomes a generator function, which doesn’t return a single value but instead returns an iterator that yields one value at a time.
- Each time `next()` is called on the generator, it runs until the next `yield` statement, then pauses, retaining its state and local variables.
- When the function is called again, it resumes from where it left off.

```python
def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i

for num in even_generator(10):
    print(num)
```
