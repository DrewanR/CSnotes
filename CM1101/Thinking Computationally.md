---
tags:
  - CM1101
---
# Computational thinking
*(quoted from [[00_computational_thinking.pdf]], using sqrt as example)*
However, all this knowledge does not help to actually find square roots!
What we need is some kind of recipe, procedure, method, algorithm for finding square roots.
There are two types of knowledge, two ways of thinking:
### “What is” knowledge
-  Statements of facts. What is true about things.
-  We call it ***declarative knowledge.***
### “How to” knowledge
-  How to do things.
-  Recipes, procedures, instructions, methods, algorithms.
-  We call it ***algorithmic knowledge.***

Create a page for declarative knowledge vs algorithmic

-->"Babylonian method” for sqrts
```
procedure SQUAREROOT(x)
Choose desired accuracy, e.g. A ← 0.0
Make an initial guess g ← x
while the error |g2 − x| > A repeat the following:
	replace g with an improved guess: g ← (g+x/g)/ 2
Finally, g is the result, i.e. g ≈ √x
end procedure
```
Works best for non integers.
Makes a guess then, if not within an appropriate error, it will do and makes an improved guess until it is within the desired accuracy

If the initial guess is zero, you end up dividing by zero... which is illegal.
## The point
When working with computers, they cant operate on declarative knowledge. Instead they have to use algorithmic knowledge.

Further questions can be asked:
	Does this method work correctly?<br>Does it always work? For all numbers? If not, when does it not work?<br>How fast does it work? How many repetitions do we need to make to reach the desired accuracy?<br>Are there faster methods to find square roots?<br>Will this method always stop?<br>How much of other resources (e.g. memory) are needed?<br>Can this method be used to solve other problems apart from square roots?