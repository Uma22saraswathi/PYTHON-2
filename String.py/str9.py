#Find all occurrences of a substring in a given string by ignoring the case
print(" Task : 9 Find all occurrences of a substring in a given string by ignoring the case")
inputstring="Rose is red and rose is beauty"
substring = "Rose"
tempstring = inputstring.lower()
count = tempstring.count(substring.lower())
print(" rose count is : ",count)