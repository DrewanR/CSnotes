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