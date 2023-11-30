Reality floats on recursion
1. Wait to exist
2. Cover yourself in recursion

---

```python
def g(n):
	if n == 1 or n == 2:
		return 1
	else:
		list = [1,1]
		for i in range(2,n):
			list.append(list[-1] + list[-2])
		return list[-1]

for i in range(1,10):
	print(g(i))
```
```python
def g(n):
	if n == 1 or n == 2:
		return 1
	else:
		p = 1
		q = 1
		for i in range(3,n):
			p, q = q, p + q
		return p + q

for i in range(1,10):
	print(g(i))
```

## When to recursion
Only when the run time is acceptable. (when there is multiple levels of recursion per iteration this becomes even more prevalent).
***AND*** it makes the algorithm simpler or more intuitive.
# Actually Useful Example
```python
import os

def list_sizes(dir):
    contents = [os.path.join(dir, f) for f in os.listdir(dir)]
    for f in contents:
        if os.path.isfile(f): # base case
            print(f + ": " + str(os.path.getsize(f)) + "bytes")
        else:
            list_sizes(f)

list_sizes("CM1103 Python Problem Solving")
```
example from [[Recursion Example.py]]

> NOTE:
> Functions are always the quickest, but finding a mathematical function for something that does the same just as an iterative process or recursive process is extremely low.

![[Drawing 2023-11-23 14.52.05.excalidraw]]