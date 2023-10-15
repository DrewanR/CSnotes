---
tags:
  - Python
  - Iteration
  - Programming
aliases:
  - Python Datatypes
Language: "[[Python]]"
---
Beware the off by one error
# While
The loop will continue as long as the condition is true. 
### Syntax
```PYTHON
while condition:
	# Keep doing this while 'condition' is True
```
### Example
```PYTHON
x = 0
while x < 10:
	x = x + 1
	print(a)
```
# For loop
Loop for every value within a [[Py Iteration#Iterable|Iterable]]
### Syntax
```PYTHON
for x in iterable:
	# Do something with x as it
	# goes (iterates) over iterable
```
### Examples
```PYTHON
for x in range(0, 5):
	print(x * x)
```
```PYTHON
for x in range(4, 12, 2):
	for power in range(2, 6):
		print(str(x) + " to the power " + str(power) + " is " + str(x ** power))
```
# Iterable
### Examples
```PYTHON
... in range(0,5)     #  0; 1; 2; 3; 4;
... in range(10,0,-2) # 10; 8; 6; 4; 2;
... in "aString"      # does it for each character in a string
... in aList          # Repeats for each index of a list
... in dictionary     # Iterated for each key in the dictionary <-->1>
```
`<-->1>` [[Py Compound Datatypes#Iterable examples|Dictionary Iteration]] you can also iterate with key value pairs