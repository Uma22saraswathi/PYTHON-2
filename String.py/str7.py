#Create a mixed string using specific rules
print(" Task : 7 : Create a mixed string using specific rules")
s1 = "Sky"
s2 = "Moon"
s3 = " "
for i in range (len(s1)):
    s3+=s1[i]
    s3+=s2[-i-1]
print(s3)
print("_______________________________________________________________")

#String characters balance test
print("String characters balance test")