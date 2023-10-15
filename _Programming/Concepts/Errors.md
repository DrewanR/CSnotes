These note have been take relative to [[Python]] if these concepts change it should be replaced.
There are three types of errors:
# Syntax Error
When you don't follow the rules or formatting of a language.
A piece of program is said to contain a syntax error if it does not conform to the syntax (rules) of the programming language.
```python
>>> print("Hello World") # This is syntactically correct
Hello World
>>> print)"Hello World") # This is syntax error
SyntaxError: unmatched ')'
```
# Run-time Error
Run-time errors are errors that might occur when a (syntactically correct) program is running, but prescribes Python to do something impossible. Potential examples:

-  Running out of memory.
-  Division by zero.
-  Accessing an element of a list that does not exist.
# Semantic Error
The program runs without any apparent errors but does not succeed at its intended task. The meaning or *semantics* of the program is wrong. The human either has devised an incorrect algorithm, or has incorrectly expressed the algorithm in form of the program.

`Example:` *You wrote a program to add the numbers 1…10, but when you run your program it adds the numbers 1…9*

# How to get rid of bugs:
Don't put them in the program in the first place
(Which isn't easy)

To do this apply the two main principles of any engineering:
## Abstraction and Composition
-  **DECOMPOSE** large problems into small, manageable parts.
	-  Each part small part (function) should be simple enough for a person to completely and fully understand how it works.
	-  Test each part thoroughly to ensure it works perfectly, as it is a lot easier to test smaller part is to ensure they are rock solid then it is to test the entire thing.
-  **COMPOSE** the large solution out of well tested solutions to sub-problems
	-  Use contracts to define how small parts fit together.
This composition can span many layers

-  Get ride of **MUTABLE STATE** where possible
	-  Use pure functions (that just compute and return a value, but do not change anything)
	-  Avoid unnecessary global variables. Keep mutable state in one place.
	-  Avoid "leaky abstractions". A function may have local mutable state, as long as this is not visible to the outside
-  Write less code, and write smarter
	-  Long, complicated code opens oneself up to bugs. Keep it simple stupid (and short... that too...)
-  Write abstractly Instead of solving a problem, solve a family of problems in the neighbourhood of the problem.
	-   Small changes to the problem should result in small changes in the solution.