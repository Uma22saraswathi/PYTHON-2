#Update the first set with items that don’t exist in the second set
a={"red","blue","green","yellow"}
b={"red","black","white","brown"}
a.difference_update(b) # same value doesn't print
print(a)