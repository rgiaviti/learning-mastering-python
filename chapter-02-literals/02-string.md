# String Literals
Python has a built-in string class named "str" with many handy features (there is an older module named "string" which you should not use). String literals can be enclosed by either double or single quotes, although single quotes are more commonly used. Backslash escapes work the usual way within both single and double quoted literals -- `e.g. \n \' \"`. A double quoted string literal can contain single quotes without any fuss (e.g. "I didn't do it") and likewise single quoted string can contain double quotes. A string literal can span multiple lines, but there must be a backslash \ at the end of each line to escape the newline. String literals inside triple quotes, """ or ''', can span multiple lines of text.

## Literals
```python
s = 'hi'                     # single quote
s = "hi"                     # double quotes
raw = r'this\t\n and that'   # raw strings

# multi-line strings
multi = """It was the best of times.
It was the worst of times."""
```

## References
- https://developers.google.com/edu/python/strings