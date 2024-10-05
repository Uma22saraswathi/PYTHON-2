#Check if a value exists in a dictionary
print("Check if a value exists in a dictionary")
my_dict={'a':10,'b':20,'c':30,}
find_value = 40
if find_value in my_dict.values():
    print(f"the value {find_value} exists in the dictionary.")
else:
    print(f"the value {find_value} does not exists in the dictionary")   
   