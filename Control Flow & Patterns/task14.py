#Reverse a given integer number
number = int(input("Enter the integer number: "))  # 12345
revs_number = 0  
while (number > 0):  
    remainder = number % 10  # 5
    revs_number = (revs_number * 10) + remainder  # 0*10=0 +5 = 5 the remainder 
    number = number // 10  
print("The reverse number is :",revs_number) 