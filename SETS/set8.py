#Update set1 by adding items from set2, except common items
set1={1,2,3,4,5}
set2={4,5,6,7,8}
common_items = set1 & set2 # use & operators, find common value {4,5}
item_add = set2 - common_items #{6,7,8} not a common value
set1 = set1 | item_add # combine set1{1,2,3,4,5} and item_add {6,7,8}
print(set1)