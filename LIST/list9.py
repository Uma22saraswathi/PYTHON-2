mylist=["apple","banana","cherry","kiwi"]
old_value="banana"
new_value="orange"
for index, value in enumerate(mylist):
    if value==old_value:
        mylist[index]=new_value
print(mylist)