## Write a Python program to find the index of an item in a specified list

x = [7,8,9,23,54]

userin = int(input('Enter a number:'))
if userin in x:
    finder = x.index(userin)
    print('The index of your number is:',finder)
else:
    print('Not in list')
   
