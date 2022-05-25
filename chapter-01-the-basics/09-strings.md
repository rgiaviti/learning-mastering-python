# Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

`'hello'` is the same as `"hello"`.

You can display a string literal with the `print()` function:

```python
print("Hello")
print('Hello')
```

```python
a = "Hello"
print(a)
```

```python
# Multi line string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# or three single quotes

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
```

## String are arrays

```python
a = "Hello, World!"
print(a[1])
```

```python
for x in "banana":
  print(x)
```

## String length

```python
a = "Hello, World!"
print(len(a))
```

## Check String

```python
txt = "The best things in life are free!"
print("free" in txt)
```

```python
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
```

## References
- https://www.w3schools.com/python/python_strings.asp