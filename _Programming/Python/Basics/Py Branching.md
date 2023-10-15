---
tags:
  - Python
  - Branching
  - Programming
aliases:
  - Python Branching
Language: "[[Python]]"
---
# If
### Syntax
```PYTHON
if condition:
	# This is executed if 'condition' is True
elif other_condition:
	# Otherwise, this is executed # (if 'other_condition' is True)
else:
	# This is executed otherwise
```
### Example
```PYTHON
pints = int(input("Pints <int>  "))
if pints > 2:
	print("You cannot drive a car!")
	if pints > 6:
		print("Call a cab!")
	else:
		print("Ride your bicycle!")
elif pints > 0:
	print("Drive very cautiously!")
else:
	print("It is ok to drive!")
```
### Extras
```PYTHON
if True:
	pass # Pass will pass, this is syntactically valid
```
