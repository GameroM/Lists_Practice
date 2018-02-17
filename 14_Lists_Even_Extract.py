## Write a Python program to print the numbers of a specified list after removing
## even numbers from it

x = [1,2,3,4,5,6,7,8,15,20,25,42]

newli = []
def evenish():
    for elem in x:
        if elem % 2 != 0:
            newli.append(elem)
    return newli
print('The original list is:', x)
print('The list without even numbers is',evenish())
