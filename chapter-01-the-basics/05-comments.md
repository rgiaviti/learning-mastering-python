# Comments in Python
Sometimes, you want to document the code that you write. For example, you may want to note why a piece of code works. To do it, you use the comments.

Typically, you use comments to explain formulas, algorithms, and complex business logic.

When executing a program, the Python interpreter ignores the comments and only interprets the code.

Python provides three kinds of comments including block comment, inline comment, and documentation string.

## Python block comments
```python
# increase price by 5%
price = price * 1.05
```

## Python inline comments
```python
salary = salary * 1.02   # increase salary by 2%
```

## Python docstrings

A documentation string is a string literal that you put as the first lines in a code block, for example, a function.

Unlike a regular comment, a documentation string can be accessed at run-time using `obj.__doc__` attribute where `obj` is the name of the function.

Typically, you use a documentation string to automatically generate the code documentation.

Documentation strings is called docstrings.

Technically speaking, docstrings are not the comments. They create anonymous variables that reference the strings. Also, they’re not ignored by the Python interpreter.

Python provides two kinds of docstrings: one-line docstrings and multi-line docstrings.

```python
def quicksort():
    """ sort the list using quicksort algorithm """
    ...
```

### Multi-line docstring
```python
def increase(salary, percentage, rating):
    """ increase salary base on rating and percentage
    rating 1 - 2 no increase
    rating 3 - 4 increase 5%
    rating 4 - 6 increase 10%
    """
```

## References
- https://www.pythontutorial.net/python-basics/python-comments/