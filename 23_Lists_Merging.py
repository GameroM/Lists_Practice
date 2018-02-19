## Write a Python program to flatten a shallow list

import itertools
x = [[2,4,3],[54,453,21],[999],[465,4562,865]]
newx = list(itertools.chain(*x))
print('The orignial list of lists is:',x)
print('When merged the new list is:',newx)
