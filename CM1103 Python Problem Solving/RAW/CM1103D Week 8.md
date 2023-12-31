# Product Rule
If an operation consists of k steps, where:
- 1st step can be performed in n<sub>1</sub> ways;
- 2nd step can be performed in n<sub>2</sub> ways
	- regardless of how 1st step was performed;
- ⋯
- kth step can be performed in n<sub>k</sub> ways
regardless of how preceding steps were performed;

Then the entire operation can be performed in n<sub>1</sub> × n<sub>2</sub> × ⋯ × n<sub>k</sub> ways.
# Sum Rule
If {S<sub>1</sub> , S<sub>2</sub> , ⋯ , S<sub>k</sub> } is a partition (see Sets handout) of a finite set S, then:
|S| = |S<sub>1</sub>| + |S<sub>2</sub>| + ⋯ + |S<sub>k</sub>|
# Permutations
A permutation of a set of objects is an order of the objects in sequence.

$$S = \set{a, b, c}$$
Permutations of S: {a, b, c} {a, c, b} {b, a, c} … (6 total permutations)

A set of n objects have n! permutations.
$$n!=n(n-1)(n-2)...*2$$
# r-permutations
An r-permutation of a set of n elements is an ordered selection of r elements taken from the set without repetition.
$$P(n,r)=\frac{n!}{(n-r)!}$$
view `itertools` in python.

# r-combinations
An r-combination of a set of size n is a subset of r

$$C(n,r) = \frac{n!}{r!(n-r)!}$$
or just use a calculator

> **R-Permutations** $P(n,r)$
> **R-Combinations** $C(n,r)$

> Split problems into easier cases then figure out the easier cases from there

### Combinational equivalence
Some counting problems can be made easier by recognising when there is a one-to-one correspondence to another problem.

# Repetition
![[Pasted image 20231123113531.png]]
![[Pasted image 20231123113639.png]]
# Indistinguishable Objects
![[Pasted image 20231123114954.png]]
