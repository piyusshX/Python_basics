# Object Types / Data Types

- Number : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10))
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

- Set : set('abc'), {'a', 'b', 'c'}

- File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')

- Boolean : True, False
- None : None
- Funtions, modules, classes

- Advance: Decorators, Generators, Iterators, MetaProgramming

##### Note - Python me kabhi bhi varible ko datatype assign nhi hota hai. Python me memory reference (jaha pe variable ki actual value save hai memory me) pe datatype assign hota hai or save hota hai.

```python
var1 = 12 # 12 is allocated in memory at some ref = x200(assigned Number datatype) and var1 is pointing x200.
print(var1) # Output -> 12

# Now if we rewrite the value of var1 then var1 will point at different reference.
var1 = "blank" # "blank" is allocated in memory at some ref = x500(assigned String datatype) and var1 is pointing x500.
print(var1) # Output -> blank
```

##### So in short, In python variables don't have any datatypes for themselves but memory locations do.
