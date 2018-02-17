## Write a Python program to print a specified list after removing the 0th, 4th
## and 5th elements.
## Sample List: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
## Sample Result: ['Green', 'White', 'Black']

x = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


x.remove(x[5])
x.remove(x[4])
x.remove(x[0])
print(x)
