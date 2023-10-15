---
tags:
  - Python
  - Datatypes
  - Programming
aliases:
  - Python Datatypes
Language: "[[Python]]"
---
Python is a weakly typed language, meaning you can change what a variables datatype easily.
[[Elementary Datatypes|Elementary Datatypes]]

In python you can see the type of a variable using `type()` e.g. `type(5) --> <type 'int'>`
You don't need to specify a type when defining a variable in python.

| Type      | Example | Convert to |
| --------- | ------- | ---------- |
| Integer   | 5       | `int(n)`   |
| Float     | 2.4     | `float(n)` |
| String    | "Cat"   | `str(n)`   |
| Character | 'e'     |            |
| Boolean   | True    |            |

Pick meaningful names, ideally describing what its used for. In python variable names may contain *letters, digits* and *underscores*. However they **must** begin in a letter.
## Selecting an index
```PYTHON
first_officer = "Spock"
first_officer[3] # "c"
first_officer[1:3] # "po"
```
**INDEXING STARTS AT 0**
# Variables in python
Python assigns a name to a value, one does not need to worry about where or how its stored. Python style guide dictates that words in variables are separated by an `_` e.g.: `stupid_system` 