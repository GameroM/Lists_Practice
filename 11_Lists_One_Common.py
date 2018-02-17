## Write a Python function that takes two lists and returns True if they have
## at least one common member

x = [1,2,3,4,5,6,7]
y = [1,2,10,11,12]
print('First list is',x)
print('Second list is', y)
li = []
def licreate():
 for elem in x:
     if elem in y:
        li.append(elem)
 return li

print('The common elements are:',licreate())

if li == []:
    print('False, no common elements in the lists')
else:
    print('True, at least one common element in the lists')
