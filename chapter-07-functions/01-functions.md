# Functions
In Python, a function is a group of related statements that performs a specific task.

Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.

Furthermore, it avoids repetition and makes the code reusable.

## Syntax

```python
def function_name(parameters):
	"""docstring"""
	statement(s)
```

## Examples

```python
def greet(name):
    """
    This function greets to the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

# calling the above function
greet('Paul')
# output:
# Hello, Paul. Good morning!
```

### Another example

*Note:* In python, the function definition should always be present before the function call. Otherwise, we will get an error. For example,

```python
# function call
greet('Paul')

# function definition
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

# Error: name 'greet' is not defined
```

## Docstrings

The first string after the function header is called the docstring and is short for documentation string. It is briefly used to explain what a function does.

Although optional, documentation is a good programming practice. Unless you can remember what you had for dinner last week, always document your code.

In the above example, we have a docstring immediately below the function header. We generally use triple quotes so that docstring can extend up to multiple lines. This string is available to us as the `__doc__` attribute of the function.

```python
>>> print(greet.__doc__)

    This function greets to
    the person passed in as
    a parameter
```

## The return statement

The return statement is used to exit a function and go back to the place from where it was called. This statement can contain an expression that gets evaluated and the value is returned. If there is no expression in the statement or the return statement itself is not present inside a function, then the function will return the None object.

```python
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))
print(absolute_value(-4))
```

## Reference
- https://www.programiz.com/python-programming/function