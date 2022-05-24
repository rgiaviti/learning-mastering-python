# For Loop
`For` loops are used when you have a block of code which you want to repeat a fixed number of times. The `for-loop` is always used in combination with an iterable object, like a list or a range. The Python for statement iterates over the members of a sequence in order, executing the block each time. Contrast the for statement with the `while` loop, used when a condition needs to be checked each iteration or to repeat a block of code forever.

## Example
```python
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
for x in range(6):
  print(x)
```

```python
for x in range(0, 3):
    print("We're on time %d" % (x))
```

The `range()` function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: `range(2, 30, 3)`:

### Nested Loops
```python
for x in range(1, 11):
    for y in range(1, 11):
        print('%d * %d = %d' % (x, y, x*y))
```

### Early exit
```python
for x in range(3):
    if x == 1:
        break
```

### For with Else
```python
for x in range(3):
    print(x)
else:
    print('Final x = %d' % (x))
```

### Strings as an iterable
```python
string = "Hello World"
for x in string:
    print(x)
```

### Lists as an iterable

```python
collection = ['hey', 5, 'd']
for x in collection:
    print(x)
```

### Loop over Lists of lists

```python
list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print(x)
```

### Creating your own iterable

```python
class Iterable(object):

    def __init__(self,values):
        self.values = values
        self.location = 0

    def __iter__(self):
        return self

    def next(self):
        if self.location == len(self.values):
            raise StopIteration
        value = self.values[self.location]
        self.location += 1
        return value
```

### Your own range generator using yield

```python
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

for x in my_range(1, 10, 0.5):
    print(x)
```

## Reference
- https://wiki.python.org/moin/ForLoop
- https://www.w3schools.com/python/python_for_loops.asp