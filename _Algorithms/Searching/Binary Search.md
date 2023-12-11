---
tags:
  - Algorithm
  - Searching
  - CM1103
algorithmType: Searching
---
A [[divide and conquer]] algorithm.
Works by eliminating half of the potential options each time but checking to see if the value in the middle of the list is greater than or less the index in the middle of the available options. Can be programmed using either iteration or recursion.

#ToDo Finish

> `Prequisits:` The list is sorted.
```python
def binarySearch(a, key, i=0, j=none):
	i = 0
	j = len(a-1)
	if i >= j:
		if a[i]
	return -1

a = range(1,50)

a = sorted(a)
print(linearSearch(a, 7))
print(linearSearch(a, 0))
```

| Complexity          | O(log n) |
| ------------------- | -------- |
| Worst case scenario |          |

You can modify the function to return the index that a given key should be inserted at.