# Tuples
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.

Tuples are:
- Unchangeable;
- Ordered;
- Allow Duplicate Values;

Tuple items are indexed, the first item has index `[0]`, the second item has index `[1]` etc.

## Examples

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```

```python
# allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
```

```python
# get tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
```

```python
# tuple with only one item
thistuple = ("apple",)
print(type(thistuple))

# this is NOT a tuple
thistuple = ("apple")
print(type(thistuple))
```

```python
# with any data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# different data types in same tuple
tuple1 = ("abc", 34, True, 40, "male")
```

## Tuple Constructor

```python
# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
```

## Reference
- https://www.w3schools.com/python/python_tuples.asp