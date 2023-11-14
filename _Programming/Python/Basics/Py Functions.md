---
tags:
  - Python
  - Programming
  - Functions
aliases:
  - Python Functions
Language: "[[Python]]"
---
A function is a named block of code.
A function should do one, thing, and do it well.
A function should be stateless, and immutable.
A function should be self contains and not leak out abstraction.
Make functions consistent: make them always return the same data type.
### In python, functions are values.
View [[Py Functions#Valuing|below]] for chaos

NOTE: Variables defined within a function are local functions.
	when referencing a name of something the local environment is checked first. Followed by the enclosing environment. Followed by the global environment.
	To avoid confusion, GIVE SENSIBLE NAMES

Functions in python can return multiple things. `return a, b` through tuples 
# Defining A Function
Functions have the same rules as variables
### Syntax
```python
def name(parameters):
	"""Optional: documentation"""
	# Insert code here
	return value
```
### Basic Example
```python
def multiply(a, b):
	"""This function multiplies two numbers"""
	result = a * b
	return result
```
### Default Values
```python
def multiply(a = 1, b = 2):
	"""This function multiplies two numbers, default: a=1 b=2."""
	...
```

---
# Advanced Examples
### Environments
```python
a = 1

def myfun(a):
	x = 2
	print("Inside: a = " + str(a))
	print("Inside: x = " + str(x))

x = 3
print("Before a call: x = " + str(x))
myfun(4)
print("After a call: x = " + str(x))
#=============================================#
"""
	Before a call: x = 3
	Inside: a = 4
	Inside: x = 2
	After a call: x = 3
"""
```
### Defaults
```python
def sum(a = 1, b = 2):
	"""This function adds two numbers. By default 1 and 2."""
	print("a is " + str(a) + ", b is " + str(b))
	sum = a + b
	return sum

print(sum())
print(sum(3))
print(sum(3, 4))
print(sum(a = 2, b = 3))
print(sum(b = 4, a = 5))
print(sum(b = 3))
```
# Valuing
Treating functions as values causes a lot of fun.
You can sparking return functions.
```python
def add(a,b):
    """ This function adds two numbers"""
    return a + b
    
def sub(a,b):
    return a - b
  
dir()
help(add)
x = 42
f = add
print(f(4,2))
funcs = [add, sub]
print(funcs[0](2,4))
print(funcs[1](3,1))
```
#ToDo HOLY SHIT THIS IS SO COOL I NEED TO PLAY WITH IT. Functions creating functions is hecking wild.
#ToDo Create a program that derives stuff from first principles.
#ToDo Look up doc test

Rough:
```python
def compose(f,g):
	def compostion(x):
		return f(g(x))
	return composition

def diff(f):
	dx = 00000.1
	def derivative(x):
		return f(x = dx) - f(x) / dx # First principles
	return derivative

d_sqr = diff(sqr)
d_sqr(4)
```

