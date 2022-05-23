# Dicts
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is *ordered*, *changeable* and *do not allow duplicates.*

## Examples

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```

```python
# duplicates are not allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
```

```python
# data types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
```

## Reference
- https://www.w3schools.com/python/python_dictionaries.asp