# Remove items from the set at once
a={"a","b","c","d","e","f"}
remove_items={"a","f"}
for item in remove_items:
    a.discard(item)
print(a)    
    
   