## Write a Python program to get a list, sorted in increasing order by the last
## element in each tuple from a given list of non-empty tuples.
## Sample List: [(2,5),(1,2),(4,4),(2,3),(2,1)]
## Sample Result: [(2,1),(1,2),(2,3),(4,4),(2,5)]

x = [(2,5),(1,2),(4,4),(2,3),(2,1)]

print(sorted(x, key=lambda x: x[1]))

## lambda just makes it so we can avoid typing function
## key = lambda followed by x:x[1]
## just means for every value in x we go to the 1th element(second in a tuple/list)
