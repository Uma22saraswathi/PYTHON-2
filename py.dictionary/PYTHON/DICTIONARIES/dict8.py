#Rename a key in a dictionary
my_dict={"oldname":"uma"}
my_dict["newname"]=my_dict.pop("oldname")
print(my_dict)