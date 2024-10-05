#Write a program to count occurrences of all characters within a string
print(" Task : 11 Write a program to count occurrences of all characters within a string")
str1="umasaraswathi"
str1_count = dict()
for i in str1:
    count=str1.count(i)
    str1_count[i] = count
print(str1_count)    
