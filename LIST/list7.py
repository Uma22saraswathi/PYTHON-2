fruits = ["apple","orange","mango",]
fruits.insert(3,"kiwi")
print(fruits)

colors = ["red","green","blue","yellow","black"]
specified_color="blue"
new_color="pink"
index = colors.index(specified_color)
colors.insert(index+1,new_color)
print(colors)