---
tags:
  - Python
  - Datatypes
  - Programming
aliases: []
Language: "[[Python]]"
---
# Tuples
Tuples are:
#### Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#### Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#### Allow Duplicates
Since tuples are indexed, they can have items with the same value

```python
thistuple = ("apple", "banana", "cherry")  
print(thistuple)
```
# Lists
***Reference data type***
Indexing starts at 0.
The elements do not need to be of consistent types.
### Syntax
```PYTHON
name = [element0, element1, element2]
```
### Example
```PYTHON
my_list = [4, False, 'Hello', ['red', 'green']]
```
### Reference data type:
#ToDo review, maybe draw diagram
Because its a reference datatype, kinda, when its passed in as a parameter it passes in a reference to the list, meaning change to the parameter effect that outside it.
`y[:]` takes a copy of a list.
#### Multidimensional
To select an index in a multidimensional array
```PYTHON
thingy = [["00","01","02","03"],
		  ["10","11","12","13"],
		  ["20","21","22","23"]]
thingy[y][x], strings show the pairs of numbers
```
#### Slicing a list
```PYTHON
[1:5] selects index   1 2 3 4   selects between the two specified elements
[ :5] selects index 0 1 2 3 4   selects up to 5
[2: ] selects index     2 3 4 5 selects from  2
[-2 ] selects index         4   selects the penultimate index
[ : ] creates slice 0 1 2 3 4 5 which is technically a seperate copy
```
https://docs.python.org/3.8/tutorial/datastructures.html
### Methods
```PYTHON
del my_list[2] # deletes index 2 (not a method). <-->1>
```
`<-->1>`[[Py Compound Datatypes#Fancy Selection|Selection]]
# Dictionary
A dictionary consists of key value pairs.
A dictionary is no defined *unordered*. As is always the case is python, the values do not need to match.
### Syntax
```PYTHON
stat_block = {"name":"Jeff", # Defining
			  "hp": 5,
			  "max_hp": 5}
stat_block ["hp"]            # Selecting
```
In the above example `"name"` is an example of a key, and `"Jeff"` is it's value.
### Iterable examples
```PYTHON
# Iterating over keys
for char in cast:
	print(char + " played by " + cast[char])
```
```PYTHON
# Iterate over keys and values in a dictionary
for char, actor in cast:
	print(char + " played by " + actor)
```