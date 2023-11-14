![[Pasted image 20231107121735.png]]
```python
a = ["a"]
a * 2     ["a","A"] 

The above will output


```

---

Avoid putting magic numbers into the code, instead use parameter or preferably a constant. This makes the code easier to change, debug and has all other wealth of benefits.

Default parameters are extra helpful and preferable as that means that the user does not need to specify a parameter value.
```python
def randomExampleFuntion(a = 300, b = "snooping as usual I see"):
	print("Executed randomExampleFuntion(", a, ", ", b,")",sep="")

randomExampleFuntion()
randomExampleFuntion(100)
randomExampleFuntion("aaaaa")
randomExampleFuntion(123332,"bbbb")
randomExampleFuntion("cccc",4324)
```

`¬((m=3)n(d=22))`
`¬(m=3)v¬(d=22))`

If you know the number of loops before hand use a for loop (definite iteration), else use indefite iteration. i.e. A `while` loop.

*Reminder: Short circuit evaluation exists. **WEAPONISE THIS***