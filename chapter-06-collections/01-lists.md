# Lists
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index `[0]`, the second item has index `[1]` etc.

When we say that lists are ordered, it means that the items have a defined order, and that order will not change. If you add new items to a list, the new items will be placed at the end of the list.

## Examples

```python
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

```python
# allow duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
```

```python
# list length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```

```python
# list items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# or different data types in same list
list1 = ["abc", 34, True, 40, "male"]
```

### List Constructor

It is also possible to use the list() constructor when creating a new list

```python
# note the double round-brackets
thislist = list(("apple", "banana", "cherry")) 
print(thislist)
```

## Access List Items

Accessing with index

```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
```

Negative Index

```python
# Access the last item of the list
print(thislist[-1])
```

Range of th indexes

```python
# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
```

```python
# This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
```

```python
# This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
```

## List Methods
| Method | Description |
|---|---|
| append() | Adds an element at the end of the list  |
| copy() | Returns a copy of the list |
| clear() | Removes all the elements from the list |
| count() | Returns the number of elements with the specified value |
| extend() | Add the elements of a list (or any iterable), to the end of the current list  |
| index() | Returns the index of the first element with the specified value |
| insert() | Adds an element at the specified position |
| pop() | Removes the element at the specified position |
| remove() | Removes the item with the specified value |
| reverse() | Reverses the order of the list |
| sort() | Sorts the list |

## Reference
- https://www.w3schools.com/python/python_lists.asp