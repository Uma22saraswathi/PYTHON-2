#Arrange string characters such that lowercase letters come first
print("task : 5 : Arrange string characters such that lowercase letters come first")
str1 = 'PyNaTive'
s = ''
S = ''
for i in str1:
    if i.islower():
        s+=i
    elif i.isupper():
        S+=i
print(s+S)
print("_______________________________________________________________")