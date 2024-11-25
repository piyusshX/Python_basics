## Number -

#### Basics Operators - 
`+` , `-` , `*` and `/`

#### `+` Operator - 
It performs addition for two numbers and concatination for two strings
```python 
2 + 3 
5               # result we get

'blan' + 'k' 
'blank'         # result we get
```

#### Exponentiation/Double-asterisk Operator `**` - 
Used for raising power over a number
```python 
2 ** 4 
16 # result we get
```

#### Floor division `//` -
Rounds the result down to the nearest whole number
```python 
15 // 2 
7 # result we get
```

#### Modulus Operator `%` - 
Gives remainder 
```python
7 % 2 
1 # result we get
```

If we want to get more than one variables simultaneously then we get a tuple of those variables

```python 
x = 2
y = 3
z = 4
x, y, z 
(2, 3, 4) # result we get
```

Python gives high precision values meaning it is really good at handling Numbers

```python 
2 ** 10  # Most languages can do this
1024

2 ** 100  # But Python can also do this
1267650600228229401496703205376

2 ** 1000 # And also this
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
```

### Comparision in Python 

#### Basic Comparisions - 

Following are the basic comparision operators in Python - `<` , `>` , `<=` , and `>=`. This is strict comparision so we cannot compare different datatypes such as string and number.

```python
5 > 6
False

10 < 14
True

10 >= 10.0
True # beacuse int and float are Number

5 > '2'
TypeError: '>' not supported between instances of 'int' and 'str'
```

#### Strict Equality `==` - 
This comparison checks both value and type (`e.g., 5 == '5' is false`).

```python
5 == '5'
False

10 == 10
True

10 == 10.0
True # beacuse int and float are Number
```

#### Not Equal `!=` - 
This comparison also checks both value and type `(e.g., 5 == '5' is true)`.

```python
5 != '5'
True

10 != 10
False

10 != 10.0
False # beacuse int and float are Number
```

#### Chained Comparisons - 

Unlike JavaScript in Python you can chain comparisons naturally, like in mathematics. 

For example, `a < b < c` means that a is less than b and b is less than c.

- `a < b < c`  == `a < b` and `b < c`

```python 
a = 3
b = 5
c = 8
a < b < c # Expression 1
True
a < b and b < c # Expression 2
True

# Exp 1 and Exp 2 are exactly same. Exp 1 shorthand notation hai Exp 2 ka.
```

### Math Library

```python 
import math
```

#### math.floor() 
It alway gives the closest bottom value than the given value.

```python
math.floor(3.5)
3
math.floor(3.7)
3
math.floor(-3.5)
-4
math.floor(-5.2)
-6
```

#### math.trunc()

It alway gives the closest value to zero then given value.

```python
math.trunc(3.5)
3
math.trunc(3.7)
3
math.trunc(-2.5)
-2
math.trunc(-5.2)
-5
```

### Different types of Numbers in Python

#### Complex Number 

Python can easily handle complex numbers and there calculations

```python
a = 2 + 1j
a * 3
(6+3j)
```

### Numbers with Octal base

Numbers with Octal base always starts with `0o`. They have values from `0 to 7`.

```python
0o20
16

0o2
2

0o16
14
```

### Numbers with Hexadecimal base

Numbers with Hexadecimal base always starts with `0x`. They have values from `0 to 9` and `A to F`.

```python
0x20
32

0x2
2

0x16
22

0xff
255

0xa
10
```

### Numbers with Binary base

Numbers with Binary base always starts with `0b`. They have only values `0 and 1`.

```python
0b1000
8

0b1001
9

0b101
5
```

### Conversion Methods

#### `oct()`

```python
oct(64) # we give decimal value and get octal val of that number
'0o100'

oct(16)
'0o20'
```

#### `hex()`

```python
hex(64)
'0x40'

hex(72)
'0x48'
```

#### `bin()`

```python
bin(4)
'0b100'

bin(15)
'0o1111'
```

#### `int()`
we can also use int method to get decimal value from binary, octal or hexadecimal value.

Syntax -> int('num', base)
```python
int('10000', 2)
16

int('20', 8)
16

int('420',16)
1056
```

### `random`
```python
import random
```

#### `random.random()`
Gives a random value between `0 and 1`
```python
random.random()
0.7970590921423096
```

#### `random.randint()`
This method gives us a random value from the given range that we have mentioned. 

Syntax -> random.randint( st-val, ed-val )

Note -> Both starting value and ending values are inclueded in the random selection.

```python
random.randint(1, 10)
6

random.randint(1, 10)
1

random.randint(1, 10)
10
```

#### `random.choice()`

Randomly selects a item/value from a given list.

```python
l1 = ['deku', 'natsu', 'yuuji']
random.choice(l1)
'natsu'
```

#### `random.shuffle()`

Shuffles the given list or items.

```python
l1 = ['deku', 'natsu', 'yuuji']
random.shuffle(l1)
l1
['natsu', 'deku', 'yuuji']
```

### Decimal calculation problem in python
Python has some problems in case of performing calculations on decimal numbers.

```python
(0.1 + 0.1 + 0.1) - 0.3 # Expected result = 0.0
5.551115123125783e-17 # Result that we got
```

To solve this problem we can import Decimal method from decimal.

```python
from decimal import Decimal
```

In Decimal method we need to give decimal values in strings otherwise the result will be  wrong.

```python
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')

Decimal('0.0') # result
```