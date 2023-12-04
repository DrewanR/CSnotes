Things to do (and not do):
1. Have variable names that don't require comments for explanation.
2. Avoid `while True`.
3. Avoid unreachably lines.
4. Typically better to return rather than print.

> In python we typically prefer to loop through items rather than indexes. Deal with the elements directly.
> The `enumerate()` function is helpful for this, enumerate() returns a tuple of the index and element.
---
# Sorting Algorithms
Just use the built in python index function.
## Linear Search
Go from the start of the list checking each element in turn

> `Prequisits:` None
```python
def linearSearch(a, key):
	for i, x in enumerate(a):
		if x == key:
			return i
	return -1

a = [2,6,7,9,4]

print(linearSearch(a, 7))
print(linearSearch(a, 0))
```

| Complexity | O(n)   |
| ---------- | --- |
| Worst case scenario | key is in index n     |

When there are multiple copies of the key it will return the first key it comes across. Can potentially add a start index to allow for searching for later editions
## Just linear for now ;-;

> *The first law of optimisation is: **Don't**
> There is a second law of optimisation, however: **Don't... yet.***
