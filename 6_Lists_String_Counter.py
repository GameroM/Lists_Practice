## Write a Python program to count the number of strings where the string length
## is 2 or more and the first and last character are same from a given list
## of strings.
## Sample list: ['abc', 'xyz', 'aba', '1221']
## Expected result: 2

x = ['abc', 'xyz', 'aba', '1221','klasjdflkasjk','lll','a'] 
li = []
def func1():
  for elem in x:
   if len(elem) >= 2 and elem[0]==elem[-1]:
    li.append(elem)
  return len(li)

print(func1())


