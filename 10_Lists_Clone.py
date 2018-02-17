## Write a Python program to clone or copy a list

x = [1,2,3,5,3,2]

print('The original list is:',x)
y = []
for elem in x:
    y.append(elem)
print('The clone of the list is:',y)
