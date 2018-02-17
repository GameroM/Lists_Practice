## Write a Python program to check if a list is empty or not

x = []
def creation():
    while True:
        
        userin=input('Enter values,type exit to stop:')
        if userin == 'exit':
            break
        else:
            x.append(userin)
    return x
print('The list created from user input is:',creation())

if x == []:
    print('The list created is empty')
else:
    print('The list created is not empty')
