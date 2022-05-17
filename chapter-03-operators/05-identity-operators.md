# Identity Operators
The identity operators in Python are used to determine whether a value is of a certain class or type. They are usually used to determine the type of data a certain variable contains. For example, you can combine the identity operators with the built-in type() function to ensure that you are working with the specific variable type.

Two identity operators are available in Python:

- **is** – returns True if the type of the value in the right operand points to the same type in the left operand. For example, type(3) is int evaluates to True because 3 is indeed an integer number.

- **is not** – returns True if the type of the value in the right operand points to a different type than the value in the left operand. For example, type(3) is not float evaluates to True because 3 is not a floating-point value.

## Examples

```python
x = 5
type(x) is int
type(x) is not float

y = 3.23
type(y) is not float
type(y) is int
```

## Reference
- https://geek-university.com/identity-operators/