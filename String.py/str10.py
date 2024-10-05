#Calculate the sum and average of the digits present in a string
print("Calculate the sum and average of the digits present in a string")

str1 = " tamil = 85 english=80 science = 85 maths = 80 history = 85" 
str2 = str1.split(' ')
nums = 0
count = 0 
for i in str2:
    if i.isdigit():
        nums+=int(i)
        count +=1
print("Total marks is :",nums)
print("average is :",nums/count)        