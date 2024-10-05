#Access value 20 from the tuple
my_tuple=(10,20,30,40,50)
if 20 in my_tuple:
    index=my_tuple.index(20)
    value = my_tuple[index]
    print(f"The value {value} is at index {index} .")
else:
    print("Value 20 is not in the tuple.")

    