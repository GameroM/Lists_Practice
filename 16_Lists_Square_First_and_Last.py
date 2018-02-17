## Write a Python program to generate and print a list of first and last 5 elements
## where the valuse are square numbers between 1 and 30

numbers = []

#def generation():
# for elem in range (1,31):
#  if elem <=5 or elem >= 26:
#   y= elem ** 2
#   numbers.append(y)
   
# return numbers

#print(generation())
    
def generation2():
    for elem in range(1,31):
        numbers.append(elem**2)
    print('The first 5 numbers squared are:',numbers[:5])
    print('The last 5 numbers squared are:',numbers[-5:])

generation2()
    
