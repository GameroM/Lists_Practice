## Write a Python program to sum all the items in a list

list1 = []

def creation():
 while True:
  userin = input('Enter values of list, type exit to stop: ')
  if userin == 'exit':
   break
  x = list1.append(int(userin))      
 return list1

#print(creation())
s = creation()
#print(s)

def addition():
    print('The list previously created is: ',s)
    x = sum(s)
    return x

print('The sum of the items in the list previously created is: ',addition())
    
