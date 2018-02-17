## Write a Python program to multiply all the items in the list

### making a list of ints
list1=[]
def creation():
 while True:
  userin = input('Enter values, type exit to stop: ')
  if userin =='exit':
   break
  x = list1.append(int(userin))
 return list1
s = creation()
print(s)

###########################
### function to multiply elements of list


def multilist():
 prod = 1
 for elem in s:
  prod *=elem
 return prod
print(multilist())

 
