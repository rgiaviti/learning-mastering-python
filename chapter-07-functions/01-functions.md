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

### Docstrings

The first string after the function header is called the docstring and is short for documentation string. It is briefly used to explain what a function does.

Although optional, documentation is a good programming practice. Unless you can remember what you had for dinner last week, always document your code.

In the above example, we have a docstring immediately below the function header. We generally use triple quotes so that docstring can extend up to multiple lines. This string is available to us as the `__doc__` attribute of the function.

```python
>>> print(greet.__doc__)

    This function greets to
    the person passed in as
    a parameter
```

### The return statement

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

### Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:

```python
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
```

### Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:

```python
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
```

### The pass statement

`function` definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

```python
def myfunction():
  pass
```


### Recursion
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, `tri_recursion()` is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

```python
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
```


## Reference
- https://www.programiz.com/python-programming/function