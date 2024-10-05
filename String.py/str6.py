# Count all letters, digits, and special symbols from a given string
print(" Task : 6 : Count all letters, digits, and special symbols from a given string")
chars = 0
digits = 0
symbols = 0
char_list =[]
digits_list =[]
symbols_list =[]

str1 = "U@#ma26t^&15h"
for i in str1:
    if i.islower() or i.isupper():
        chars+=1
        char_list .append(i)
     
    elif i.isnumeric():
        digits+=1
        digits_list.append(i)
        
    else:
        symbols +=1
        symbols_list.append(i)
print('chars:',chars,char_list)
print('digits:',digits,digits_list)
print('symbol:',symbols,symbols_list) 
print("_______________________________________________________________")