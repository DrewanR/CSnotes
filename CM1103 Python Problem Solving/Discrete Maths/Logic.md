---
tags:
  - CM1103
  - DiscreteMaths
  - Maths
---
#ToDo Make coherent

Logic concerns principles is correct reasoning.
[[Logic_handout.pdf|View handout]]
# Propositional Logic
*A **proposition** is a sentence declaring a fact that is either **True** or **False***
#### Examples
Stuart Allen is the module leader of CM1103. P
Cardiff is the capital of France. P
8 + 2 = 10 P
8 + 2 = 15 P
Is it Tuesday? NP
Read this. NP
n < 5 NP
If n is 4, then n < 5 P
# Combining propositions
Compound propositions are formed from other propositions using logical operators.
![[Pasted image 20231030143451.png]]
## Negation `¬`
Let 𝑝 be a proposition. The negation of 𝑝, denoted ¬𝑝, is the statement “It is not the case that 𝑝”.
## Conjunction `Ʌ` and Disjunction `V`
**Conjunction:** *and*
**Disjunction:** *or*

Let 𝑝 and 𝑞 be propositions. The conjunction of 𝑝 and 𝑞, denoted 𝑝 Ʌ 𝑞, is the proposition “𝑝 and 𝑞”. It is true if both 𝑝 and 𝑞 are true, and false otherwise.
Let 𝑝 and 𝑞 be propositions. The disjunction of 𝑝 and 𝑞, denoted 𝑝 V 𝑞, is the proposition “𝑝 or 𝑞”. It is true if either 𝑝 or 𝑞 (or both) are true, and false otherwise.

```
p = False, q = True
p Ʌ q = False
p V q = True
```
---
#### Example
`NOTE:` Truth table notes have been omitted as I already know them
Truth tables allow us to add more operands
Must include all the possible combinations

| p   | q   | r   | p Ʌ q | ¬r  | (pɅq)V¬r    |
| --- | --- | --- |:-----:|:---:|:---:|
| 0   | 0   | 0   |   0   |  1  | 1    |
| 0   | 0   | 1   |   0   |  0  | 0    |
| 0   | 1   | 0   |   0   |  1  | 1    |
| 0   | 1   | 1   |   0   |  0  | 0    |
| 1   | 0   | 0   |   0   |  1  | 1    |
| 1   | 0   | 1   |   0   |  0  | 0    |
| 1   | 1   | 0   |   1   |  1  | 1    |
| 1   | 1   | 1   |   1   |  0  | 1    |

---
## Logic in python
```Python
¬ = not
Ʌ = and
V = or
```
## Short Circuit Evaluation
*Present in [[Python]], amongst lots of other languages*
When a Boolean operation is evaluated, the second argument is only executed or evaluated if the first ones does not suffice to determine the outcome.

**AND** *If the first argument is false, it returns false without executing the other argument*
**OR** *If the first argument is true, it wont evaluate the second argument*

Because of this, it makes sense to put the simplest arguments first and more complex ones afterwards.
