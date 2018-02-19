## Write a Python program to generate and print a list EXCEPT for the first 5
## elements, where the square of numbers between 1 and 30.

li = []
for elem in range(1,31):
     x= elem**2
     li.append(x)
print(li[5:])
