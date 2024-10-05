#Check if two sets have any elements in common. If yes, display the common elements
names={"uma","divya","sara","lara"}
names1={"uma","divya"}
common_names= names.intersection(names1)
if common_names:
    print("common Names : ",common_names)
else:
    print("no common names in the sets")    
