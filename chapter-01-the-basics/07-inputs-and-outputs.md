# Inputs and Outputs
Python provides numerous built-in functions that are readily available to us at the Python prompt.

Some of the functions like `input()` and `print()` are widely used for standard input and output operations respectively. Let us see the output section first.

## Output
We use the `print()` function to output data to the standard output device (screen). We can also output data to a file, but this will be discussed later.

An example of its use is given below.

```python
print("Hey! Hello from Python")
print("You name is", "Joe")
print(1,3,5,7,8, sep="*", end="&")
```

### Formatting

```python
x = 10
y = 20
print("The value of x is {} and the value of y is {}".format(x, y))
```

Another example

```python
print("Hi {name}, {greet}".format(greet="Welcome", name="Ricardo"))
```

## Input
Up until now, our programs were static. The value of variables was defined or hard coded into the source code.

To allow flexibility, we might want to take the input from the user. In Python, we have the `input()` function to allow this. The syntax for `input()` is:

```python
my_name = input()
print("Hello ", my_name)
```

## References
- https://www.programiz.com/python-programming/input-output-import