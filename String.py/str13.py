#Find the last position of a given substring
print("Find the last position of a given substring")
test_string="Gfg is best for cs and also best for learning"
target_word = "best"
print("the originl string :"+str(test_string))
res=test_string.rfind(target_word)
print("index of last occurrence of substring is :"+str(res))
