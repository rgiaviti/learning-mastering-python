# Sets
Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is *unordered*, *unchangeable*, and *unindexed*.

## Examples

```python
thisset = {"apple", "banana", "cherry"}
print(thisset)
```

```python
# Duplicates are not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
```

```python
# Data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
```

```python
# Different data types
set1 = {"abc", 34, True, 40, "male"}
```

## Constructor

```python
# note the double round-brackets
thisset = set(("apple", "banana", "cherry"))
print(thisset)
```

## Reference
- https://www.w3schools.com/python/python_sets.asp