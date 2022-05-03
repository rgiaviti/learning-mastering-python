# Python Data Types

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

## Built-In Data Types
These data types are already included with Python Programming Languages
```
Text Type:         str
Numeric Types:     int, float, complex
Sequence Types:    list, tuple, range
Mapping Type:      dict
Set Types:         set, frozenset
Boolean Type:      bool
Binary Types:      bytes, bytearray, memoryview
None Type:         NoneType
```

## Getting the Data Type
```python
x = 5
print(type(x))
```

## Implicit assignments for each Data Type

```python
x = "Hello World"                              # str	
x = 20                                         # int	
x = 20.5                                       # float	
x = 1j                                         # complex	
x = ["apple", "banana", "cherry"]              # list	
x = ("apple", "banana", "cherry")              # tuple	
x = range(6)                                   # range	
x = {"name" : "John", "age" : 36}              # dict	
x = {"apple", "banana", "cherry"}              # set	
x = frozenset({"apple", "banana", "cherry"})   # frozenset	
x = True                                       # bool	
x = b"Hello"                                   # bytes	
x = bytearray(5)                               # bytearray	
x = memoryview(bytes(5))                       # memoryview	
x = None                                       # NoneType
```

## Explicit assignments for each Data Type

```python
x = str("Hello World")                         # str	
x = int(20)                                    # int	
x = float(20.5)                                # float	
x = complex(1j)                                # complex	
x = list(("apple", "banana", "cherry"))        # list	
x = tuple(("apple", "banana", "cherry"))       # tuple	
x = range(6)                                   # range	
x = dict(name="John", age=36)                  # dict	
x = set(("apple", "banana", "cherry"))         # set	
x = frozenset(("apple", "banana", "cherry"))   # frozenset	
x = bool(5)                                    # bool	
x = bytes(5)                                   # bytes	
x = bytearray(5)                               # bytearray	
x = memoryview(bytes(5))                       # memoryview
```

## Another way to assign variables
```python
# single assigment
age = 10
name = "Joe"

# multi assignment
country, city, year = "Brazil", "São José do Rio Preto", 2022

# output
print(name, age)
print("The player name is ", name, " and his age is ", age)
```

## References
- https://www.w3schools.com/python/python_datatypes.asp