## Write a Python program to get the largest number from a list

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


def maxnum():
 maxx = max(s)
 return maxx

print(maxnum())
