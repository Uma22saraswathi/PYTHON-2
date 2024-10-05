#Remove items from set1 that are not common to both set1 and set2
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.intersection_update(set2)
print("Updated set1:", set1)
