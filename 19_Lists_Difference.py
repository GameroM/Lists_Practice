## Write a Python program to get the difference between two lists.

x = [1,2,3,4,5]
y = [1,3,5,7]

z = []
z2 = []
#def check1():
for elem in x:
 if elem not in y:
  z.append(elem)
print('The elements in the first list that are not in 2nd list are:',z)

#x = check1()

#def check2():
for elem in y:
 if elem not in x:
  z2.append(elem)
print('Elements in second list not in 1st list are:',z2)
#y = check2()

print('The list that contains the differences is:',z+z2)
            

