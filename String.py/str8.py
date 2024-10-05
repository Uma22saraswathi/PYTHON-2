# String characters balance test
print("String characters balance test")
s1 = "uma"
s2 = "umasaraswathi"
s3 = True
for i in s1:
    if i in s2:
        s3 = True
    else:
        s3 = False
        break
print(s3)        