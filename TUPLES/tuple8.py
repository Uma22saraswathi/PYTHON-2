#Sort a tuple of tuples by the 2nd item
my_tuples= ((1, 'banana'), (3, 'apple'), (2, 'orange'))
sorted_tuple = sorted(my_tuples, key=lambda x: x[1])
print(sorted_tuple) 
