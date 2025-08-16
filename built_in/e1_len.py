def myfunc(n):
  return len(n)

# map (function, iterable). 
# len use to count how many characters in a string. or length of a list or tuple blah blah
x = map(myfunc, ('apple', 'banana', 'cherry'))

#convert the map into a list, for readability:
print(list(x))
