---
tags:
  - Python
  - Programming
aliases:
  - Python String Manipulation
Language: "[[Python]]"
---
```PYTHON
s.lower() # Makes lower case
s.upper() # Makes upper case
s.strip() # Removes whitespace
s.isalpha(); s.isdigit; s.isspace # Tests if the string is all one thing
s.startswith("no") # Tests if the string begins with another string
s.endswith("no") # ... end of string
s.find("string") # Searches for the first occurance of "string", -1 = not present
s.replace("old", "new") # Replaces the old with the new
```
https://docs.python.org/3/library/stdtypes.html#string-methods contains a longer list.

Note: the `in` keyword exists.