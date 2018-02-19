## Write a Python program to generate all permutations of a list in Python.
## (all possible combinations of list)

import itertools
x = itertools.permutations([1,2,3])
y = list(x)
print(y)
