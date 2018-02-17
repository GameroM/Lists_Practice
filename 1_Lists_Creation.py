## Write a python program to create a list with user input


lis = []
def list1():
 while True: 
  userin = input('Enter strings of list:')
  x = lis.append(userin)
  if userin == 'exit':
     lis.remove('exit')
     break
 print(lis)

list1()
