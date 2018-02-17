## Write a Python program to get the smallest number in a list

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

def minnum():
 minn= min(s)
 return minn
print(minnum())
