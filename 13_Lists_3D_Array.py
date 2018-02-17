## Write a Python program to generate a 3*4*6 3D array whose each element is *

x = [[['*' for col in range(10)] for col in range(4)]for row in range(3)]
print(x)

## first part of list comprehension is number of * in every list, afterwards its
## just a row by column print, looks a bit weird on print but thats just because
## no space,(has to be fullscreen to get full effect of 3*4
