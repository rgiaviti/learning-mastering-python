# Importing Modules

Import in python is similar to #include header_file in C/C++. Python modules can get access to code from another module by importing the file/function using import. The import statement is the most common way of invoking the import machinery, but it is not the only way.

import module_name 
When the import is used, it searches for the module initially in the local scope by calling `__import__()` function. The value returned by the function is then reflected in the output of the initial code. 

## Examples

```python
import math
print(math.pi)
print(math.e)
```

Another example

```python
from math import pi, e
print(pi)
print(e)
```

## References
- https://www.geeksforgeeks.org/import-module-python